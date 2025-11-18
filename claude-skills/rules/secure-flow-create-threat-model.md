---
description: Perform comprehensive, lightweight threat modeling analysis of specified component, service, or application. Practical, developer-focused, actionable.
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

rule_id: secure-flow-create-threat-model

## Create Threat Model

Help perform comprehensive, lightweight threat modeling analysis of specified component, service, or application. Practical, developer-focused, actionable.

### Component Analysis
- Understand component (type, purpose, technology stack, dependencies, data flow, user interactions)
- Identify attack surfaces:
  - **Data entry points**: API endpoints, user input, webhooks, message queues, file imports, external APIs, configuration, command line
  - **Trust boundaries**: authentication, network, service, privilege, data, process
  - **External dependencies**: libraries, APIs, cloud services, databases, message brokers, CDNs, auth providers
  - **Data storage/transmission**: databases, file systems, caches, logs, network, backups

### STRIDE Threat Analysis
- **Spoofing**: user/service/identity spoofing (weak/missing authentication, session hijacking, credential theft)
- **Tampering**: data in transit/at rest, configuration/code tampering (missing integrity checks, weak encryption, missing access controls)
- **Repudiation**: user/system actions, transaction repudiation (missing audit logs, inadequate logging, no non-repudiation)
- **Information Disclosure**: data/log/error exposure, side channels (insecure APIs, missing access controls, inadequate encryption, stack traces, timing attacks)
- **Denial of Service**: resource exhaustion (CPU, memory, disk, connections), application/network/dependency DoS (missing rate limiting, expensive operations, DDoS, external API failures)
- **Elevation of Privilege**: privilege escalation (missing authorization, weak access controls, horizontal/vertical escalation, code execution)

### Prioritized Threat Analysis
- For each threat:
  - **Attack scenario**: steps, prerequisites, example
  - **Likelihood assessment**: attack complexity, required skills, attack surface, existing controls, motivation
  - **Impact assessment**: data/system/business/compliance/reputation impact
  - **Risk rating**: likelihood × impact, priority
  - **Current mitigations**: what exists, effectiveness, gaps
  - **Recommended mitigations**: immediate/short-term/long-term actions, implementation, cost/benefit

### Top 3-5 Abuse Cases
- Prioritize most likely high impact, high impact lower likelihood, common attack patterns, business-critical, compliance violations
- For each: attack vector, impact, detection, prevention, response
- Make practical, developer-focused, actionable
- Focus on real threats with specific, implementable recommendations

### Implementation Checklist
- [ ] Analyzed component and identified attack surfaces
- [ ] Performed STRIDE threat analysis
- [ ] Assessed likelihood and impact for each threat
- [ ] Identified current mitigations and gaps
- [ ] Recommended immediate, short-term, and long-term mitigations
- [ ] Prioritized top 3-5 abuse cases
- [ ] Provided specific, implementable recommendations

