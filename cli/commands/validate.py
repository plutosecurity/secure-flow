"""
Validate command - Validate all rule files
"""
from ..core.validator import RuleValidator


def validate_rules() -> int:
    """Validate all rule files"""
    print("Validating all rule files...\n")
    
    results = RuleValidator.validate_all_rules()
    
    if not results:
        print("No rule files found to validate.")
        return 0
    
    valid_count = sum(1 for is_valid, _ in results.values() if is_valid)
    total_count = len(results)
    
    for rule_name, (is_valid, errors) in sorted(results.items()):
        if is_valid:
            print(f"✅ {rule_name}")
        else:
            print(f"❌ {rule_name}")
            for error in errors:
                print(f"   - {error}")
    
    print(f"\nValidation complete: {valid_count}/{total_count} rules are valid")
    
    return 0 if valid_count == total_count else 1

