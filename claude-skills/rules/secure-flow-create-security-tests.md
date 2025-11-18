---
description: Generate security-focused unit tests for specified routes, functions, or components. Verify security assumptions and catch vulnerabilities.
languages:
- python
- javascript
- typescript
- java
- go
- ruby
- php
- csharp
alwaysApply: false
---

rule_id: secure-flow-create-security-tests

## Create Security Tests

Help generate security-focused unit tests for specified routes, functions, or components. Verify security assumptions and catch vulnerabilities.

### Code Analysis
- Identify security boundaries (authentication requirements, authorization checks, input validation points, access control logic, trust boundaries)
- Security features (authentication, authorization, input validation, output encoding, error handling, rate limiting, session management, CSRF protection, security headers)
- Attack vectors (authentication/authorization bypass, injection attacks, access control bypass, session hijacking, CSRF, information disclosure)

### Comprehensive Test Cases
- Generate tests for:
  - **Authentication**: valid/invalid credentials, expired tokens, missing tokens, SQL injection/XSS in username
  - **Authorization**: authorized/unauthorized access, role escalation, IDOR, path traversal
  - **Input validation**: SQL injection, XSS, command injection, path traversal, LDAP/XML injection, edge cases
  - **Access control**: resource ownership, permission boundaries, bypass attempts
  - **Rate limiting**: within/exceeding limits, per-user/IP
  - **Error handling**: no stack traces, no sensitive data, generic errors
  - **Session management**: creation, expiration, invalidation, hijacking prevention
  - **CSRF protection**: valid/invalid/missing tokens

### Test Framework Integration
- Use appropriate framework (pytest, Jest, JUnit, etc.)
- Organize tests clearly (AAA pattern, isolation, setup/teardown)
- Create mocks for external dependencies (authentication, database, external APIs, file system, network)
- Generate complete, runnable test code covering all security aspects, edge cases, and attack vectors
- Use appropriate testing frameworks and follow best practices

### Implementation Checklist
- [ ] Analyzed code for security boundaries and features
- [ ] Identified attack vectors
- [ ] Generated authentication test cases
- [ ] Generated authorization test cases
- [ ] Generated input validation test cases
- [ ] Generated access control test cases
- [ ] Generated rate limiting test cases
- [ ] Generated error handling test cases
- [ ] Generated session management test cases
- [ ] Generated CSRF protection test cases
- [ ] Integrated with appropriate test framework
- [ ] Created mocks for external dependencies
- [ ] Ensured complete, runnable test code

