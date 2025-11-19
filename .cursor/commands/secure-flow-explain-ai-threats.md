# Explain AI Threats

## Overview

Help perform comprehensive security analysis of AI-powered application components. Identify AI-specific security threats and provide remediation guidance.

## Steps

1. **AI Security Risk Identification**
    - Identify prompt injection (direct user input injection, system prompt override, instruction injection, indirect data/file/API injection, jailbreaking, role-playing)
    - Data exfiltration (training data extraction, system data leakage, output manipulation)
    - Insecure plugin/function calls (plugin injection, function call manipulation, plugin security)
    - Training data extraction (memorization, membership inference, model inversion)
    - Model manipulation (model poisoning, adversarial examples, model extraction)
    - Jailbreaking (safety bypass, role manipulation, instruction following)
    - Prompt leakage (system prompt exposure, prompt reconstruction)
    - System prompt override (user prompt dominance, instruction injection)
2. **Code Analysis**
    - Analyze input sanitization/validation (prompt construction, user input handling, input validation/sanitization/encoding)
    - Prompt construction/escaping (system/user prompt construction, prompt escaping/isolation/validation)
    - Output filtering/sanitization (output filtering/sanitization, sensitive data detection, output validation/encoding)
    - Plugin/function call validation (call/parameter validation, permission checks, sandboxing/isolation)
    - Rate limiting/abuse prevention (rate limiting, abuse detection, throttling, cost controls, usage monitoring)
    - Context isolation (context separation, session/user/data isolation)
    - User input handling (input validation/sanitization/encoding, length limits, type checking)
3. **Remediation Strategies**
    - Secure prompt engineering (clear prompt structure, instruction separation, input validation, output constraints, safety instructions)
    - Input/output validation (validate inputs/outputs, type/range/format checking)
    - Sandboxing/isolation (process/container/network isolation, resource limits, permission restrictions)
    - Monitoring/detection (anomaly detection, attack detection, pattern analysis, alerting, logging)
    - Access controls (authentication, authorization, rate limiting, usage quotas, cost controls)
    - Make analysis practical with real attack examples and concrete fixes
    - Focus on actionable remediation
    - Show before/after code examples demonstrating secure patterns

## Explain AI Threats Checklist

- [ ] Identified AI-specific security risks
- [ ] Analyzed prompt injection vulnerabilities
- [ ] Analyzed data exfiltration risks
- [ ] Analyzed plugin/function call security
- [ ] Analyzed input/output validation
- [ ] Analyzed rate limiting and abuse prevention
- [ ] Analyzed context isolation
- [ ] Provided secure prompt engineering strategies
- [ ] Provided sandboxing and isolation recommendations
- [ ] Provided monitoring and detection guidance
- [ ] Showed before/after code examples
- [ ] Focused on actionable remediation
