# Gate Critical Vulnerabilities

## Overview

Set up CI/CD checks to block the inclusion of critical vulnerabilities to your codebase. Create or update a CI workflow that runs Trivy filesystem scanning to detect critical vulnerabilities and fail the pipeline if any are introduced.

## Steps

1. **Workflow Setup**
    - Check if there is already a Trivy workflow in the repository
    - If workflow exists, add the new step to the existing workflow
    - If no workflow exists, create a new workflow file
    - Configure workflow to run on every PR to the default branch

2. **Trivy Configuration**
    - Use only Trivy filesystem scanning via the aquasecurity/trivy-action GitHub Action
    - Do not integrate with other security tools
    - Configure Trivy to scan for critical severity vulnerabilities
    - Set workflow to fail if critical vulnerabilities are introduced

3. **Detailed Logging**
    - Add detailed logging to show the vulnerabilities found
    - Display vulnerability details including:
        - CVE ID
        - Package name and version
        - Severity level
        - Description
        - Fixed version (if available)
    - Show user what needs to be updated

4. **Remediation**
    - If the CI fails due to critical vulnerabilities, patch the dependencies
    - Update vulnerable packages to fixed versions
    - Ensure the PR is ready to merge after remediation
    - Verify the pipeline passes after fixes are applied

## Gate Critical Vulnerabilities Checklist

- [ ] Checked for existing Trivy workflow in repository
- [ ] Created or updated workflow file
- [ ] Configured Trivy filesystem scan for critical vulnerabilities
- [ ] Set workflow to run on every PR to default branch
- [ ] Added detailed logging for vulnerability details
- [ ] Configured workflow to fail on critical vulnerabilities
- [ ] Tested workflow detects critical vulnerabilities
- [ ] Patched dependencies if vulnerabilities found
- [ ] Verified pipeline passes after remediation

