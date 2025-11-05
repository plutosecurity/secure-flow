# Fix Vulnerability

## Overview

Help fix identified security vulnerability while preserving functionality. Provide complete, tested solution.

## Steps

1. **Vulnerability Analysis**
    - Identify vulnerability type (CWE, OWASP, CVSS, severity)
    - Understand vulnerable code (functionality, inputs, outputs, dependencies)
    - Analyze attack surface (attack vectors, trust boundaries)
2. **Safe Remediation Strategy**
    - Preserve functionality (maintain behavior, don't break APIs, backward compatibility)
    - Choose right fix (framework-provided secure alternatives, defense in depth, industry standards)
    - Implement fix (refactor to secure patterns, add validation/sanitization, output encoding, security headers, secure defaults)
3. **Code Changes**
    - Show exact fix with complete before/after code
    - Include imports/dependencies
    - Add security comments (why fix is necessary, CWE/OWASP reference)
    - Handle edge cases (boundary conditions, error cases, no new vulnerabilities)
4. **Testing and Verification**
    - Test fix prevents vulnerability
    - Ensure existing functionality works
    - Test edge cases and error paths
    - Show how to test fix, provide example test cases, suggest security testing approaches
5. **Additional Security Enhancements**
    - Consider input validation beyond immediate fix
    - Output encoding, security headers (CSP, HSTS), rate limiting
    - Logging/monitoring, secure error handling, defense in depth measures
    - Provide complete, production-ready code that fixes the vulnerability while maintaining all existing functionality

## Fix Vulnerability Checklist

- [ ] Identified vulnerability type and severity
- [ ] Analyzed vulnerable code and attack surface
- [ ] Chose appropriate fix preserving functionality
- [ ] Implemented fix with complete before/after code
- [ ] Added security comments and references
- [ ] Handled edge cases and error paths
- [ ] Tested fix prevents vulnerability
- [ ] Verified existing functionality works
- [ ] Considered additional security enhancements
- [ ] Provided production-ready code
