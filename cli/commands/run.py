"""
Run command - Run a specific rule manually with LLM assistance
"""
import sys
from pathlib import Path
from typing import List, Optional

from ..core.config import RULES_DIR
from ..core.llm_client import LLMClient


def run_rule(
    rule_id: str,
    files: List[str],
    llm_token: Optional[str],
    provider: str
) -> int:
    """Run a specific rule manually with LLM assistance"""
    
    # Find rule file
    rule_file = RULES_DIR / f"{rule_id}.md"
    if not rule_file.exists():
        # Try without prefix
        rule_file = RULES_DIR / f"secure-flow-{rule_id}.md"
        if not rule_file.exists():
            print(f"Error: Rule '{rule_id}' not found in {RULES_DIR}", file=sys.stderr)
            return 1
    
    # Read rule content
    try:
        rule_content = rule_file.read_text()
    except Exception as e:
        print(f"Error reading rule file: {e}", file=sys.stderr)
        return 1
    
    # Read file contents for context
    codebase_context = {}
    if files:
        for filepath in files:
            file_path = Path(filepath)
            if not file_path.exists():
                print(f"Warning: File not found: {filepath}", file=sys.stderr)
                continue
            
            try:
                content = file_path.read_text()
                codebase_context[str(file_path)] = content
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
    else:
        print("No files specified. Running rule without codebase context.", file=sys.stderr)
    
    # Execute rule with LLM
    try:
        print(f"Executing rule '{rule_id}' using {provider}...\n")
        llm = LLMClient(provider=provider, api_key=llm_token)
        result = llm.run_rule(rule_content, codebase_context)
        
        print("=" * 80)
        print("RULE EXECUTION RESULT")
        print("=" * 80)
        print(result)
        print("=" * 80)
        return 0
    except Exception as e:
        print(f"Error executing rule: {e}", file=sys.stderr)
        return 1

