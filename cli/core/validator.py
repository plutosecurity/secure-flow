"""
Rule validation module
"""
import yaml
import re
from pathlib import Path
from typing import List, Dict, Tuple

from .config import RULES_DIR


class RuleValidator:
    """Validates rule files for proper structure"""
    
    REQUIRED_FIELDS = ['description', 'languages', 'alwaysApply']
    REQUIRED_CONTENT = ['rule_id']
    
    @staticmethod
    def validate_rule_file(rule_path: Path) -> Tuple[bool, List[str]]:
        """Validate a single rule file"""
        errors = []
        
        if not rule_path.exists():
            return False, [f"File does not exist: {rule_path}"]
        
        content = rule_path.read_text()
        
        # Check for frontmatter
        if not content.startswith('---'):
            errors.append("Missing frontmatter (should start with '---')")
            return False, errors
        
        # Parse frontmatter
        try:
            frontmatter_end = content.index('---', 3)
            frontmatter_text = content[3:frontmatter_end].strip()
            frontmatter = yaml.safe_load(frontmatter_text)
            
            if not frontmatter:
                errors.append("Frontmatter is empty or invalid YAML")
                return False, errors
            
            # Check required fields
            for field in RuleValidator.REQUIRED_FIELDS:
                if field not in frontmatter:
                    errors.append(f"Missing required frontmatter field: {field}")
            
            # Validate alwaysApply is boolean
            if 'alwaysApply' in frontmatter and not isinstance(frontmatter['alwaysApply'], bool):
                errors.append("'alwaysApply' must be a boolean")
            
            # Validate languages is a list
            if 'languages' in frontmatter and not isinstance(frontmatter['languages'], list):
                errors.append("'languages' must be a list")
            
        except ValueError:
            errors.append("Invalid frontmatter format (missing closing '---')")
        except yaml.YAMLError as e:
            errors.append(f"Invalid YAML in frontmatter: {e}")
        
        # Check for rule_id in content
        if 'rule_id:' not in content:
            errors.append("Missing 'rule_id:' field in content")
        else:
            # Extract rule_id
            rule_id_match = re.search(r'rule_id:\s*(\S+)', content)
            if rule_id_match:
                rule_id = rule_id_match.group(1)
                # Validate rule_id matches filename
                expected_rule_id = rule_path.stem
                if rule_id != expected_rule_id:
                    errors.append(f"rule_id '{rule_id}' does not match filename '{expected_rule_id}'")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_all_rules() -> Dict[str, Tuple[bool, List[str]]]:
        """Validate all rule files"""
        results = {}
        
        if not RULES_DIR.exists():
            return results
        
        for rule_file in RULES_DIR.glob("*.md"):
            is_valid, errors = RuleValidator.validate_rule_file(rule_file)
            results[str(rule_file.name)] = (is_valid, errors)
        
        return results

