# Secure Flow CLI

A command-line interface for managing and executing Secure Flow security rules.

## Installation

1. Navigate to the CLI directory:
```bash
cd cli
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your LLM API key (choose one):
```bash
# For Anthropic Claude
export ANTHROPIC_API_KEY="your-api-key-here"

# For OpenAI
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

**Note:** All commands should be run from the `cli/` directory using `python main.py`, or use `python cli/main.py` from the project root.

The CLI uses argparse and is organized into folders:

**Structure:**
```
cli/
├── main.py             # Executable entry point script
├── cli.py              # Main entry point with argument parsing
├── core/               # Core functionality modules
│   ├── config.py       # Configuration constants
│   ├── validator.py    # Rule validation logic
│   └── llm_client.py   # LLM API integration
└── commands/           # Command handlers (one file per command)
    ├── list.py         # List command
    ├── create.py       # Create command
    ├── validate.py     # Validate command
    └── run.py          # Run command
```

### List All Rules

List all existing security rules:

```bash
# From cli/ directory
python main.py list
# or
python -m cli.cli list

# Or from project root
python cli/main.py list
# or
python -m cli.cli list

# Or with help
python main.py --help
python main.py list --help
```

Example output:
```
Found 10 rule(s):

  📋 secure-flow-fix-exploitable-vulns
     Description: Fix CISA Known Exploited Vulnerabilities (KEV) if exists in your codebase...
     Languages: python, javascript, typescript, java, go, ruby, php, csharp, docker, yaml
     Always Apply: false
```

### Create a New Rule

Create a new rule with LLM assistance using codebase context:

```bash
# From cli/ directory
python main.py create "my-new-rule" \
  --description "Description of what this rule does" \
  --files ../src/main.py ../src/utils.py \
  --languages python javascript \
  --llm-token "your-api-key" \
  --provider anthropic

# Or from project root (use relative paths from root)
python cli/main.py create "my-new-rule" \
  --description "Description of what this rule does" \
  --files src/main.py src/utils.py \
  --languages python javascript \
  --llm-token "your-api-key" \
  --provider anthropic
```

Options:
- `--description, -d`: Required. Description of the rule
- `--files, -f`: Specific files to include as context (can be used multiple times)
- `--llm-token, -t`: LLM API token (optional if env var is set)
- `--provider, -p`: LLM provider: `anthropic` (default) or `openai`
- `--languages, -l`: Target languages (default: python, javascript, typescript)
- `--output, -o`: Output file path (default: auto-generated from rule name)

Example:
```bash
python cli.py create "validate-api-security" \
  --description "Validate API endpoints for security best practices" \
  --files api/routes.py api/middleware.py \
  --languages python \
  --provider anthropic
```

### Validate All Rules

Validate all rule files for proper structure:

```bash
# From cli/ directory
python main.py validate

# Or from project root
python cli/main.py validate
```

This checks:
- Frontmatter format and required fields
- Rule ID matches filename
- Proper YAML syntax
- Required content fields

Example output:
```
Validating all rule files...

✅ secure-flow-fix-exploitable-vulns.md
✅ secure-flow-create-secure-template.md
❌ secure-flow-invalid-rule.md
   - Missing required frontmatter field: description
   - rule_id 'wrong-id' does not match filename 'secure-flow-invalid-rule'

Validation complete: 9/10 rules are valid
```

### Run a Specific Rule

Execute a specific rule manually with LLM assistance:

```bash
# From cli/ directory
python main.py run secure-flow-fix-exploitable-vulns \
  --files ../package.json ../src/index.js \
  --llm-token "your-api-key" \
  --provider anthropic

# Or from project root
python cli/main.py run secure-flow-fix-exploitable-vulns \
  --files package.json src/index.js \
  --llm-token "your-api-key" \
  --provider anthropic
```

Options:
- `--files, -f`: Specific files to include as context (can be used multiple times)
- `--llm-token, -t`: LLM API token (optional if env var is set)
- `--provider, -p`: LLM provider: `anthropic` (default) or `openai`

The rule ID can be specified with or without the `secure-flow-` prefix:
- `secure-flow-fix-exploitable-vulns` ✅
- `fix-exploitable-vulns` ✅

Example:
```bash
python cli.py run fix-exploitable-vulns \
  --files requirements.txt src/main.py \
  --provider anthropic
```

## Rule File Structure

Rules must follow this structure:

```markdown
---
description: Brief description of the rule
languages:
- python
- javascript
alwaysApply: false
---

rule_id: secure-flow-rule-name

## Rule Title

Detailed description and instructions...

### Section 1
- Step 1
- Step 2

### Implementation Checklist
- [ ] Task 1
- [ ] Task 2
```

## Environment Variables

- `ANTHROPIC_API_KEY`: Anthropic Claude API key
- `OPENAI_API_KEY`: OpenAI API key

## Examples

### Create a rule for Docker security
```bash
# From project root
python cli/main.py create "docker-security-scan" \
  --description "Scan Dockerfiles for security vulnerabilities" \
  --files Dockerfile docker-compose.yml \
  --languages docker yaml \
  --provider anthropic
```

### Run a rule on specific files
```bash
# From project root
python cli/main.py run validate-compliance \
  --files src/auth.py src/database.py \
  --provider anthropic
```

### Validate all rules before committing
```bash
# From project root
python cli/main.py validate
```

## Troubleshooting

**Error: No API key provided**
- Set the `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` environment variable, or use `--llm-token`

**Error: anthropic package not installed**
- Run: `pip install anthropic`

**Error: Rule not found**
- Use `python cli.py list` to see all available rules
- Rule IDs are case-sensitive

**Error: Invalid frontmatter**
- Ensure frontmatter is valid YAML between `---` markers
- Check that all required fields are present

