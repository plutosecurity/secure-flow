# Explain Risk

## Overview

Help analyze provided code or security finding and provide comprehensive, educational explanation. Transform static scanner output into actionable security knowledge.

## Steps

1. **Context Analysis**
    - Examine code context: vulnerability type (CWE ID, OWASP Top 10, CVSS score)
    - What vulnerable code accomplishes, surrounding patterns and dependencies
    - Framework/library/language used
2. **Why It Matters - Risk Assessment**
    - Explain security risk: threat classification (CWE category, e.g., CWE-79: XSS, CWE-89: SQL Injection, CWE-502: Deserialization)
    - Attack vector (how attacker could exploit)
    - Impact assessment (data compromised, system affected, business impact: financial, reputational, compliance)
    - Likelihood (ease of exploitation, public accessibility, authentication required, compensating controls)
    - Industry context (OWASP, NIST, CWE references)
3. **Real-World Attack Scenarios**
    - Provide concrete attack scenarios: step-by-step exploitation
    - Example malicious inputs/payloads
    - Demonstrate attack in context of actual code
    - Explain what attacker could achieve (data theft, system compromise, privilege escalation)
    - Reference real-world examples of similar vulnerabilities
4. **Root Cause Analysis**
    - Explain why vulnerability exists: common developer mistakes leading to issue
    - Why secure alternatives exist
    - Framework/library considerations
    - Missing security controls or validation
5. **How to Fix It - Detailed Remediation**
    - Provide complete solution: immediate fix (exact code change needed)
    - Safer alternative (secure replacement, e.g., yaml.safe_load() instead of yaml.load())
    - Migration path (if changing APIs)
    - Defense in depth (input validation, output encoding, security headers, monitoring)
    - Code examples (before/after snippets with explanations)
    - Testing (how to verify fix works, doesn't break functionality)
6. **Prevention and Best Practices**
    - Provide guidance: secure coding patterns for vulnerability type
    - Code review checklist items
    - Static analysis rules
    - Developer training recommendations
    - Make explanation educational, actionable, context-aware
    - Use codebase context for specific examples
    - Turn security finding into learning opportunity

## Explain Risk Checklist

- [ ] Analyzed code context and vulnerability type
- [ ] Assessed security risk and impact
- [ ] Identified attack vectors
- [ ] Provided real-world attack scenarios
- [ ] Performed root cause analysis
- [ ] Provided immediate fix with code examples
- [ ] Suggested safer alternatives and migration path
- [ ] Recommended defense in depth measures
- [ ] Provided testing guidance
- [ ] Included prevention and best practices
- [ ] Made explanation educational and actionable
