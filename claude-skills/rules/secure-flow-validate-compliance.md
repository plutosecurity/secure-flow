---
description: Help validate the current code context against compliance requirements (SOC 2, ISO 27001, NIST, GDPR, HIPAA, PCI DSS). Identify gaps, validate controls, and provide remediation guidance.
languages:
- python
- javascript
- typescript
- java
- go
- ruby
- php
- csharp
- terraform
- yaml
alwaysApply: false
---

rule_id: secure-flow-validate-compliance

## Validate Compliance

Help validate the current code context against compliance requirements (SOC 2, ISO 27001, NIST, GDPR, HIPAA, PCI DSS). Identify gaps, validate controls, and provide remediation guidance.

### Compliance Framework Identification
- Identify applicable frameworks: SOC 2, ISO 27001, NIST CSF, GDPR, HIPAA, PCI DSS, FedRAMP, CCPA, CIS Controls
- Understand application type, data types, deployment environment, and geographic scope

### Compliance Control Validation
- **Access control**: MFA, RBAC, least privilege, session management
- **Encryption**: HTTPS/TLS, data at rest, key management
- **Logging**: security events, audit trails, retention
- **Configuration**: debug mode, security headers, CORS, secrets
- **Vulnerability management**: scanning, patching, remediation
- **Data privacy**: data minimization, consent, PII handling
- **Incident response**: detection, response plan, escalation
- **Business continuity**: backups, recovery procedures

### Code Context Analysis
- Analyze authentication, authorization, encryption, logging, configuration, error handling, input validation, session management, and secret management
- Compare against requirements and identify:
  - Missing controls
  - Inadequate controls
  - Misconfigured controls
  - Non-compliant code

### Compliance Validation Report
- **Executive summary**: status, findings count, compliance score, recommendations
- **Framework-specific validation**: control status, evidence, gaps, recommendations
- **Detailed findings**: severity, location, impact, remediation steps
- **Prioritized remediation roadmap**: P0-P3
- Generate actionable compliance validation with specific code locations, before/after examples, and prioritized remediation steps

### Implementation Checklist
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

