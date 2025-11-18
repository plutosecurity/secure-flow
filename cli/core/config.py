"""
Configuration constants for Secure Flow CLI
"""
from pathlib import Path

# CLI is in cli/ folder, so go up two levels to find claude-skills (cli/core -> cli -> root)
RULES_DIR = Path(__file__).parent.parent.parent / "claude-skills" / "rules"
SKILL_FILE = Path(__file__).parent.parent.parent / "claude-skills" / "SKILL.md"

