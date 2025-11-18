---
description: Run a security remediation task that checks for vulnerabilities in the codebase and applies necessary fixes. Scan the codebase for vulnerabilities using Trivy and attempt to fix up to 3 vulnerabilities of the highest impact.
languages:
- python
- javascript
- typescript
- java
- go
- ruby
- php
- csharp
- docker
- yaml
alwaysApply: false
---

rule_id: secure-flow-security-remediation

## Security Remediation

Run a security remediation task that checks for vulnerabilities in the codebase and applies necessary fixes. Scan the codebase for vulnerabilities using Trivy and attempt to fix up to 3 vulnerabilities of the highest impact.

### Vulnerability Scanning
- Run Trivy filesystem scan on the codebase
- Use command: `trivy fs --format json <path to repo directory>`
- Parse the JSON output to identify vulnerabilities
- Sort vulnerabilities by impact/severity

### Vulnerability Analysis
- Identify the highest impact vulnerabilities
- Select up to 3 vulnerabilities to remediate
- Analyze each vulnerability:
  - CVE ID
  - Severity level
  - Affected package and version
  - Available fixed version
  - Impact assessment

### Remediation Planning
- Determine the fix strategy for each vulnerability
- Check if fixed versions are available
- Plan dependency updates or patches needed
- Consider impact on application functionality

### Apply Fixes
- Update vulnerable packages to fixed versions
- Apply patches if available
- Update dependency files (requirements.txt, package.json, etc.)
- Ensure backward compatibility where possible

### Verification
- Re-run Trivy scan to verify vulnerabilities are fixed
- Test that application functionality still works
- Verify no new vulnerabilities were introduced
- Document fixes applied

### Implementation Checklist
- [ ] Ran Trivy filesystem scan on codebase
- [ ] Parsed Trivy JSON output
- [ ] Identified highest impact vulnerabilities
- [ ] Selected up to 3 vulnerabilities to fix
- [ ] Analyzed each vulnerability's details
- [ ] Planned remediation strategy
- [ ] Updated vulnerable packages to fixed versions
- [ ] Updated dependency files
- [ ] Re-ran Trivy scan to verify fixes
- [ ] Tested application functionality
- [ ] Verified no new vulnerabilities introduced
- [ ] Documented fixes applied

