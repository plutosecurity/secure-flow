---
description: Create complete, production-ready, secure boilerplate templates for requested patterns or frameworks. Secure by default, follows industry best practices.
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

rule_id: secure-flow-create-secure-template

## Create Secure Template

Help create complete, production-ready, secure boilerplate template for requested pattern or framework. Secure by default, follows industry best practices.

### Template Requirements Analysis
- Understand requested pattern (framework/language, application type, deployment environment, security requirements)
- Identify security requirements (authentication, authorization, data protection, compliance needs)

### Framework-Specific Security Best Practices
- **Python**: Security headers/middleware, JWT with secure signing, RBAC, input validation (Pydantic/Marshmallow), secrets management, secure defaults (DEBUG=False, HTTPS enforced), logging with secret masking
- **Node.js**: Helmet.js, CORS, rate limiting, JWT with secure signing, input validation (Joi/Yup)
- **Terraform**: S3 encryption, IAM least privilege, network security

### Complete Template Structure
- Provide project structure (app/, tests/, config/, .env.example)
- Configuration management (environment-based, secure defaults, secrets management)
- Authentication (JWT, token refresh, password reset, MFA support)
- Authorization (RBAC, permission checking, resource-level)
- Input validation (schema validation, type checking, range validation)
- Security headers (CSP, HSTS, X-Frame-Options, etc.)
- Error handling (secure error messages, proper status codes)
- Logging/monitoring (security events, audit trails, secret masking)
- Database security (encrypted connections, parameterized queries, least privilege)
- API security (rate limiting, input validation, CORS)
- Testing infrastructure (unit/integration/security tests)
- CI/CD security (secret scanning, dependency scanning, SAST)

### Code Implementation
- Include complete, working code examples for main application setup
- Authentication endpoints, protected endpoints, input validation
- Error handling, security headers, logging, database connection
- Provide complete, production-ready code following security best practices from day one
- Include comments explaining security decisions
- Template should be immediately usable and secure by default

### Implementation Checklist
- [ ] Analyzed template requirements and security needs
- [ ] Applied framework-specific security best practices
- [ ] Created complete project structure
- [ ] Implemented configuration management with secure defaults
- [ ] Added authentication and authorization
- [ ] Implemented input validation and security headers
- [ ] Added error handling and logging/monitoring
- [ ] Configured database and API security
- [ ] Included testing infrastructure
- [ ] Added CI/CD security scanning
- [ ] Provided complete, working code examples
- [ ] Included security decision comments

