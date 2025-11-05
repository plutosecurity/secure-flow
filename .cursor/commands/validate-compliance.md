# Validate Compliance

## Overview

Help validate the current code context against compliance requirements (SOC 2, ISO 27001, NIST, GDPR, HIPAA, PCI DSS). Identify gaps, validate controls, and provide remediation guidance.

## Steps

1. **Compliance Framework Identification**
    - Identify applicable frameworks: SOC 2, ISO 27001, NIST CSF, GDPR, HIPAA, PCI DSS, FedRAMP, CCPA, CIS Controls
    - Understand application type, data types, deployment environment, and geographic scope
2. **Compliance Control Validation**
    - Check access control (MFA, RBAC, least privilege, session management)
    - Encryption (HTTPS/TLS, data at rest, key management)
    - Logging (security events, audit trails, retention)
    - Configuration (debug mode, security headers, CORS, secrets)
    - Vulnerability management (scanning, patching, remediation)
    - Data privacy (data minimization, consent, PII handling)
    - Incident response (detection, response plan, escalation)
    - Business continuity (backups, recovery procedures)
3. **Code Context Analysis**
    - Analyze authentication, authorization, encryption, logging, configuration, error handling, input validation, session management, and secret management
    - Compare against requirements and identify missing controls, inadequate controls, misconfigured controls, and non-compliant code
4. **Compliance Validation Report**
    - Provide executive summary (status, findings count, compliance score, recommendations)
    - Framework-specific validation (control status, evidence, gaps, recommendations)
    - Detailed findings (severity, location, impact, remediation steps)
    - Prioritized remediation roadmap (P0-P3)
    - Generate actionable compliance validation with specific code locations, before/after examples, and prioritized remediation steps

## Validate Compliance Checklist

- [ ] Identified applicable compliance frameworks
- [ ] Validated access control and authentication
- [ ] Validated encryption and key management
- [ ] Validated logging and audit trails
- [ ] Validated configuration security
- [ ] Validated vulnerability management
- [ ] Validated data privacy controls
- [ ] Validated incident response procedures
- [ ] Validated business continuity
- [ ] Analyzed code context for compliance gaps
- [ ] Generated compliance validation report
- [ ] Provided prioritized remediation roadmap
