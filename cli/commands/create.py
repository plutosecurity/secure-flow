"""
Create command - Create a new rule with LLM assistance
"""
import sys
from pathlib import Path
from typing import List, Optional

from ..core.config import CURSOR_COMMANDS_DIR, RULES_DIR
from ..core.llm_client import LLMClient


def create_rule(
    rule_name: str,
    description: str,
    files: List[str],
    llm_token: Optional[str],
    provider: str,
    languages: List[str],
    output: Optional[str]
) -> int:
    """Create a new rule with LLM assistance using codebase context"""
    
    # Read file contents
    files_content = {}
    if files:
        for filepath in files:
            file_path = Path(filepath)
            if not file_path.exists():
                print(f"Warning: File not found: {filepath}", file=sys.stderr)
                continue
            
            try:
                content = file_path.read_text()
                files_content[str(file_path)] = content
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
    
    if not files_content:
        print("No valid files provided. Creating rule without codebase context.", file=sys.stderr)
    
    # Generate rule with LLM
    try:
        print(f"Generating rule '{rule_name}' using {provider}...")
        llm = LLMClient(provider=provider, api_key=llm_token)
        rule_content = llm.generate_rule(
            rule_name=rule_name,
            description=description,
            files_content=files_content,
            languages=languages
        )
    except Exception as e:
        print(f"Error generating rule: {e}", file=sys.stderr)
        return 1
    
    # Determine output path
    if not output:
        rule_id = f"secure-flow-{rule_name.lower().replace(' ', '-').replace('_', '-')}"
        output_path = RULES_DIR / f"{rule_id}.md"
    else:
        output_path = Path(output)
    
    # Ensure rules directory exists
    RULES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Write rule file
    try:
        output_path.write_text(rule_content)
        print(f"✅ Rule created successfully: {output_path}")
    except Exception as e:
        print(f"Error writing rule file: {e}", file=sys.stderr)
        return 1
    
    # Generate and write cursor command file
    try:
        print(f"Generating cursor command file using {provider}...")
        
        # Determine cursor command filename - use the same name as the rule file that was created
        rule_filename = output_path.stem  # Get filename without extension
        cursor_command_name = rule_filename  # Use the same name as the rule file
        
        cursor_command_path = CURSOR_COMMANDS_DIR / f"{cursor_command_name}.md"
        
        # Ensure cursor commands directory exists
        CURSOR_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Generate cursor command content using AI
        cursor_command_content = llm.generate_cursor_command(rule_content, rule_name)
        
        # Remove markdown code block wrapper if present
        content = cursor_command_content.strip()
        if content.startswith('```markdown'):
            content = content[11:]  # Remove ```markdown
        elif content.startswith('```'):
            content = content[3:]  # Remove ```
        
        # Remove trailing ```
        if content.endswith('```'):
            content = content[:-3]
        
        cursor_command_content = content.strip()
        
        # Write cursor command file
        cursor_command_path.write_text(cursor_command_content)
        print(f"✅ Cursor command created successfully: {cursor_command_path}")
        return 0
    except Exception as e:
        print(f"Warning: Error creating cursor command file: {e}", file=sys.stderr)
        # Don't fail the whole operation if cursor command creation fails
        return 0

