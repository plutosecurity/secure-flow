"""
LLM client module for interacting with AI providers
"""
import os
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
    
    def run_rule(self, rule_content: str, codebase_context: Dict[str, str]) -> str:
        """Execute a rule with codebase context"""
        
        files_context = "\n\n".join([
            f"## File: {filepath}\n```\n{content}\n```"
            for filepath, content in codebase_context.items()
        ])
        
        prompt = f"""You are executing a Secure Flow security rule. Follow the rule instructions precisely and apply them to the provided codebase context.

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
        
        if self.provider == "anthropic":
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=8192,
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
                max_tokens=8192
            )
            return response.choices[0].message.content

