"""
LLM client module for interacting with AI providers
"""
import os
import sys
from typing import Dict, List, Optional

# Try to import LLM libraries
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


class LLMClient:
    """Client for interacting with LLM APIs"""
    
    # Model context limits (conservative estimates)
    MAX_CONTEXT_TOKENS = 8192
    SAFE_INPUT_TOKENS = 3000  # Reserve for input (rule + prompt overhead)
    SAFE_OUTPUT_TOKENS = 4096  # Reserve for output
    SAFETY_MARGIN = 500  # Extra margin for token estimation errors
    
    def __init__(self, provider: str = "anthropic", api_key: Optional[str] = None):
        self.provider = provider.lower()
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY") or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError(f"No API key provided. Set {provider.upper()}_API_KEY environment variable or pass --llm-token")
        
        if self.provider == "anthropic":
            if not HAS_ANTHROPIC:
                raise ImportError("anthropic package not installed. Install with: pip install anthropic")
            self.client = anthropic.Anthropic(api_key=self.api_key)
        elif self.provider == "openai":
            if not HAS_OPENAI:
                raise ImportError("openai package not installed. Install with: pip install openai")
            self.client = openai.OpenAI(api_key=self.api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}. Use 'anthropic' or 'openai'")
    
    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """Estimate token count (rough approximation: ~4 chars per token)"""
        return len(text) // 4
    
    def _calculate_max_tokens(self, input_tokens: int) -> int:
        """Calculate safe max_tokens based on input size"""
        available = self.MAX_CONTEXT_TOKENS - input_tokens - self.SAFETY_MARGIN
        # Ensure we have at least some output capacity, but cap at safe output limit
        return max(1000, min(available, self.SAFE_OUTPUT_TOKENS))
    
    def _split_codebase_context(self, codebase_context: Dict[str, str], max_tokens_per_chunk: int) -> List[Dict[str, str]]:
        """Split codebase context into chunks that fit within token limits"""
        chunks = []
        current_chunk = {}
        current_tokens = 0
        
        for filepath, content in codebase_context.items():
            file_header = f"## File: {filepath}\n```\n"
            file_footer = "\n```\n\n"
            file_header_tokens = self._estimate_tokens(file_header + file_footer)
            content_tokens = self._estimate_tokens(content)
            
            # If single file is too large, truncate it
            if content_tokens > max_tokens_per_chunk - file_header_tokens - 100:
                # Truncate to fit
                max_content_chars = (max_tokens_per_chunk - file_header_tokens - 100) * 4
                content = content[:max_content_chars] + "\n... [truncated due to size] ...\n"
                content_tokens = self._estimate_tokens(content)
            
            # Check if adding this file would exceed chunk limit
            if current_tokens + file_header_tokens + content_tokens > max_tokens_per_chunk and current_chunk:
                chunks.append(current_chunk)
                current_chunk = {}
                current_tokens = 0
            
            current_chunk[filepath] = content
            current_tokens += file_header_tokens + content_tokens
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks if chunks else [{}]
    
    def generate_rule(self, rule_name: str, description: str, files_content: Dict[str, str], languages: List[str]) -> str:
        """Generate a new rule using LLM"""
        
        files_context = "\n\n".join([
            f"## File: {filepath}\n```\n{content[:2000]}...\n```"
            for filepath, content in files_content.items()
        ])
        
        prompt = f"""You are creating a security rule for Secure Flow, a security framework for AI coding agents.

Rule Name: {rule_name}
Description: {description}
Target Languages: {', '.join(languages)}

Relevant Codebase Context:
{files_context}

Create a complete rule file following this structure:

1. Frontmatter (YAML between --- markers):
   - description: Brief description of the rule
   - languages: List of applicable languages
   - alwaysApply: false (boolean)

2. Content:
   - rule_id: secure-flow-{rule_name.lower().replace(' ', '-')}
   - Title as H2 heading
   - Detailed description
   - Sections with subsections (use ### for subsections)
   - Implementation Checklist at the end with checkboxes

The rule should be comprehensive, actionable, and follow the same style as existing Secure Flow rules. Focus on security best practices, specific steps, and clear implementation guidance.

Return ONLY the complete markdown file content, starting with the frontmatter."""
        
        if self.provider == "anthropic":
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            return message.content[0].text
        else:  # openai
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                max_tokens=4096
            )
            return response.choices[0].message.content
    
    def _make_api_call(self, prompt: str, max_tokens: int) -> str:
        """Make a single API call to the LLM"""
        if self.provider == "anthropic":
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=max_tokens,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            return message.content[0].text
        else:  # openai
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
    
    def run_rule(self, rule_content: str, codebase_context: Dict[str, str]) -> str:
        """Execute a rule with codebase context, splitting into multiple calls if needed"""
        
        # Estimate tokens for rule and base prompt
        base_prompt_template = """You are executing a Secure Flow security rule. Follow the rule instructions precisely and apply them to the provided codebase context.

## Rule to Execute:
{rule_content}

## Codebase Context:
{files_context}

Execute this rule step by step:
1. Analyze the codebase context against the rule requirements
2. Identify what needs to be done according to the rule
3. Provide specific, actionable guidance
4. If code changes are needed, provide the complete updated code
5. Follow the implementation checklist in the rule

Be thorough, specific, and actionable. Focus on security best practices."""
        
        rule_tokens = self._estimate_tokens(rule_content)
        base_prompt_tokens = self._estimate_tokens(base_prompt_template.replace("{rule_content}", "").replace("{files_context}", ""))
        
        # Calculate available tokens for codebase context
        available_for_context = self.SAFE_INPUT_TOKENS - rule_tokens - base_prompt_tokens
        
        # Build files context
        files_context = "\n\n".join([
            f"## File: {filepath}\n```\n{content}\n```"
            for filepath, content in codebase_context.items()
        ])
        context_tokens = self._estimate_tokens(files_context)
        
        # If context fits in one call, do it
        if context_tokens <= available_for_context:
            prompt = base_prompt_template.format(
                rule_content=rule_content,
                files_context=files_context
            )
            input_tokens = self._estimate_tokens(prompt)
            max_tokens = self._calculate_max_tokens(input_tokens)
            return self._make_api_call(prompt, max_tokens)
        
        # Otherwise, split into chunks and make multiple calls
        print(f"Codebase context is large ({context_tokens} estimated tokens). Splitting into chunks...", file=sys.stderr)
        
        chunks = self._split_codebase_context(codebase_context, available_for_context)
        results = []
        
        for i, chunk in enumerate(chunks, 1):
            chunk_files_context = "\n\n".join([
                f"## File: {filepath}\n```\n{content}\n```"
                for filepath, content in chunk.items()
            ])
            
            if len(chunks) > 1:
                chunk_prompt = f"""You are executing a Secure Flow security rule. This is part {i} of {len(chunks)}.

## Rule to Execute:
{rule_content}

## Codebase Context (Part {i} of {len(chunks)}):
{chunk_files_context}

Analyze this portion of the codebase against the rule requirements. Provide specific findings and actionable guidance for this part. Focus on security best practices."""
            else:
                chunk_prompt = base_prompt_template.format(
                    rule_content=rule_content,
                    files_context=chunk_files_context
                )
            
            input_tokens = self._estimate_tokens(chunk_prompt)
            max_tokens = self._calculate_max_tokens(input_tokens)
            
            print(f"Processing chunk {i}/{len(chunks)}...", file=sys.stderr)
            chunk_result = self._make_api_call(chunk_prompt, max_tokens)
            results.append(chunk_result)
        
        # If multiple chunks, combine results with a summary call
        if len(chunks) > 1:
            combined_results = "\n\n".join([
                f"## Chunk {i+1} Results:\n{result}"
                for i, result in enumerate(results)
            ])
            
            summary_prompt = f"""You are executing a Secure Flow security rule. The codebase was analyzed in {len(chunks)} parts. Combine and synthesize the findings below into a comprehensive, actionable response.

## Rule to Execute:
{rule_content}

## Analysis Results from All Chunks:
{combined_results}

Provide a unified, comprehensive response that:
1. Synthesizes all findings from the chunked analysis
2. Provides a complete picture of what needs to be done
3. Includes all specific, actionable guidance
4. Presents any code changes needed in a complete, unified format
5. Follows the implementation checklist in the rule

Be thorough, specific, and actionable. Focus on security best practices."""
            
            summary_tokens = self._estimate_tokens(summary_prompt)
            max_tokens = self._calculate_max_tokens(summary_tokens)
            return self._make_api_call(summary_prompt, max_tokens)
        
        return results[0] if results else ""

