# Trace Secret

## Overview

Help perform comprehensive security audit of how a secret (API key, token, password, credential) is handled throughout the codebase. Trace complete lifecycle.

## Steps

1. **Secret Identification**
    - Identify secret (variable name, type, initial location)
    - Understand scope (multiple services, environments, versions)
2. **Complete Lifecycle Analysis**
    - Trace secret loading (environment variables, config files, secrets managers, hardcoded values, cloud metadata)
    - Storage (in-memory, file system, database, sessions, caches, encrypted storage)
    - Usage (API calls, database connections, authentication, encryption, service-to-service)
    - Transmission (network requests, URLs, headers, WebSocket, logging, error messages)
    - Exposure (application logs, debug statements, error handling, stack traces, API responses, version control, documentation)
3. **Security Risk Assessment**
    - Assess risks: plaintext storage (high - use encryption), logging exposure (critical - never log secrets), insecure transmission (critical - use HTTPS, never in URLs), hardcoded values (critical - use environment variables/secrets managers), insufficient encryption (high - use strong encryption), insufficient access control (high - least privilege), no rotation policy (medium - implement rotation), shared secrets (high - use unique secrets)
4. **Comprehensive Recommendations**
    - Immediate: remove from logs, rotate if exposed, remove from version control, revoke exposed secrets
    - Short-term: use secrets management (AWS Secrets Manager, Vault, Key Vault), implement secret masking, secure transmission (HTTPS, secure headers), encryption at rest
    - Long-term: secret rotation, access control (IAM roles, audit logging), monitoring/alerting, security scanning
    - Generate comprehensive report with executive summary, lifecycle map, detailed findings (file paths, code snippets, risk assessment, recommendations), risk matrix, and remediation plan

## Trace Secret Checklist

- [ ] Identified secret and its scope
- [ ] Traced secret loading and storage
- [ ] Traced secret usage and transmission
- [ ] Identified all exposure points
- [ ] Assessed security risks for each lifecycle stage
- [ ] Provided immediate remediation steps
- [ ] Provided short-term improvements
- [ ] Provided long-term security enhancements
- [ ] Generated comprehensive report with lifecycle map
- [ ] Created risk matrix and remediation plan
