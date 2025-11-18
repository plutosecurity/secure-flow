"""
Create command - Create a new rule with LLM assistance
"""
import sys
from pathlib import Path
from typing import List, Optional

from ..core.config import RULES_DIR
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
        return 0
    except Exception as e:
        print(f"Error writing rule file: {e}", file=sys.stderr)
        return 1

