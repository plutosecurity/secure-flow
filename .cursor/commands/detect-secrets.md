# Detect Secrets

## Overview

Detect secrets and credentials in your codebase using gitleaks on a selected location. Scan for API keys, passwords, tokens, and other sensitive information that should not be committed to version control. This command will alert you about detected secrets but will not modify or remove any code.

## Steps

1. **Verify Gitleaks Installation**
    - Check if gitleaks is installed and available in PATH
    - Verify with: `gitleaks version`
    - If not installed, provide installation instructions

2. **Run Gitleaks Scan**
    - Use `gitleaks detect` command to scan the selected location
    - Specify the source directory with `--source` flag
    - Use `--report-format json` for structured output
    - Save report with `--report-path` flag (e.g., `gitleaks-report.json`)
    - For non-git directories, add `--no-git` flag
    - Use `--verbose` for detailed output

3. **Parse and Display Results**
    - Parse the JSON report to extract findings
    - Display summary of detected secrets
    - For each finding, show:
        - File path and line number
        - Secret type (Rule ID)
        - Description of the secret type
        - Matched content (redacted or truncated for security)
        - Commit information (if git repository)

4. **Alert User**
    - Clearly indicate if secrets were found
    - Provide detailed information about each detected secret
    - Explain the risk associated with each finding
    - Recommend actions (rotate credentials, remove from code, use secret management)
    - Do NOT modify, remove, or rotate any code or credentials

5. **Report Generation**
    - Save the full report for user review
    - Provide the report file path
    - Ensure report is readable and actionable

## Example Command

```bash
gitleaks detect --source . --report-format json --report-path gitleaks-report.json --verbose
```

## Detect Secrets Checklist

- [ ] Verified gitleaks is installed
- [ ] Identified target location to scan
- [ ] Ran gitleaks detect with appropriate flags
- [ ] Parsed JSON report for findings
- [ ] Displayed summary of detected secrets
- [ ] Listed details for each finding (file, line, type, description)
- [ ] Alerted user about detected secrets
- [ ] Provided recommendations for remediation
- [ ] Saved report file for user review
- [ ] Did NOT modify or remove any code

