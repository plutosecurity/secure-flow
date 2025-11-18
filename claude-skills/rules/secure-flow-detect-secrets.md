---
description: Detect secrets and credentials in your codebase using gitleaks on a selected location. Scan for API keys, passwords, tokens, and other sensitive information that should not be committed to version control.
languages:
- python
- javascript
- typescript
- java
- go
- ruby
- php
- csharp
- yaml
- json
- shell
alwaysApply: false
---

rule_id: secure-flow-detect-secrets

## Detect Secrets with Gitleaks

Detect secrets and credentials in your codebase using gitleaks on a selected location. Scan for API keys, passwords, tokens, and other sensitive information that should not be committed to version control.

### Prerequisites
- Ensure gitleaks is installed and available in PATH
- Installation: https://github.com/gitleaks/gitleaks#installing
- Verify with: `gitleaks version`

### Running Gitleaks Scan
- Use `gitleaks detect` command to scan for secrets
- Specify the source directory with `--source` flag
- Use `--report-format json` for structured output
- Save report with `--report-path` flag
- For non-git directories, add `--no-git` flag
- Use `--verbose` for detailed output

### Basic Scan Command
```bash
gitleaks detect --source /path/to/scan --report-format json --report-path gitleaks-report.json
```

### Custom Configuration
- Create a `.gitleaks.toml` config file for custom rules
- Specify config with `--config` flag
- Customize rules, allowlists, and ignore patterns
- Example: `gitleaks detect --source . --config .gitleaks.toml`

### Understanding Results
- Gitleaks exit codes:
  - 0: No secrets found (success)
  - 1: Secrets detected (action required)
  - 2: Error occurred during scan
- Review JSON report for detailed findings
- Each finding includes:
  - File path and line number
  - Secret type and rule ID
  - Matched content (redacted in output)
  - Commit information (if git repository)

### Alerting on Detected Secrets
- **Alert the user** about any detected secrets
- Display detailed information for each finding:
  - File path and line number
  - Secret type (Rule ID) and description
  - Risk level and impact assessment
- Provide recommendations for remediation (but do NOT execute them)
- Recommend rotating exposed credentials (user must do this manually)
- Suggest using secret management solutions (AWS Secrets Manager, HashiCorp Vault, etc.)
- Do NOT modify, remove, or rotate any code or credentials

### CI/CD Integration
- Add gitleaks scan to CI/CD pipeline
- Fail builds when secrets are detected
- Use GitHub Action: `gitleaks/gitleaks-action@v2`
- Example GitHub Actions workflow:
```yaml
- name: Gitleaks Scan
  uses: gitleaks/gitleaks-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Best Practices
- Run gitleaks before committing code
- Add pre-commit hooks to prevent accidental commits
- Scan entire repository periodically
- Keep gitleaks configuration up to date
- Educate team on secret management
- Use `.gitignore` for sensitive files

### Example Gitleaks Config (.gitleaks.toml)
```toml
[extend]
useDefault = true

[allowlist]
description = "Allowlisted files"
paths = [
  '''\.md$''',
  '''go.sum$''',
  '''package-lock\.json$'''
]

[allowlist]
description = "Allowlisted secrets"
regexes = [
  '''EXAMPLE_API_KEY''',
  '''fake-secret-for-testing'''
]
```

### Implementation Checklist
- [ ] Verified gitleaks is installed
- [ ] Identified target directory/path to scan
- [ ] Ran gitleaks detect with appropriate flags
- [ ] Parsed JSON report for findings
- [ ] Displayed summary of detected secrets
- [ ] Listed details for each finding (file, line, type, description)
- [ ] Alerted user about detected secrets
- [ ] Provided recommendations for remediation
- [ ] Saved report file for user review
- [ ] Did NOT modify or remove any code

