"""
List command - List all existing rules
"""
import sys
import yaml
import re
from pathlib import Path

from ..core.config import RULES_DIR


def list_rules() -> int:
    """List all existing rules"""
    if not RULES_DIR.exists():
        print("Rules directory not found!", file=sys.stderr)
        return 1
    
    rules = sorted(RULES_DIR.glob("*.md"))
    
    if not rules:
        print("No rules found.")
        return 0
    
    print(f"\nFound {len(rules)} rule(s):\n")
    
    for rule_file in rules:
        try:
            content = rule_file.read_text()
            
            # Extract frontmatter
            if content.startswith('---'):
                frontmatter_end = content.index('---', 3)
                frontmatter_text = content[3:frontmatter_end].strip()
                frontmatter = yaml.safe_load(frontmatter_text)
                
                description = frontmatter.get('description', 'No description')
                languages = ', '.join(frontmatter.get('languages', []))
                always_apply = frontmatter.get('alwaysApply', False)
                
                # Extract rule_id
                rule_id_match = re.search(r'rule_id:\s*(\S+)', content)
                rule_id = rule_id_match.group(1) if rule_id_match else rule_file.stem
                
                print(f"  📋 {rule_id}")
                print(f"     Description: {description}")
                print(f"     Languages: {languages}")
                print(f"     Always Apply: {always_apply}")
                print()
        except Exception as e:
            print(f"  ⚠️  {rule_file.name} (error reading: {e})")
            print()
    
    return 0

