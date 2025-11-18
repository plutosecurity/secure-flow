---
description: Review API authentication and authorization mechanisms. Find API endpoints on this service that have no authentication attached to them and add authentication where missing.
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

rule_id: secure-flow-review-api-auth

## API Authentication Review

Review API authentication and authorization mechanisms. Find API endpoints on this service that have no authentication attached to them and add authentication where missing.

### Endpoint Discovery
- Identify all API endpoints in the service
- Create a comprehensive list of all API endpoints
- Document endpoint locations, methods, and routes

### Authentication Mechanism Detection
- Check if the project has any authentication mechanisms
- Identify authentication frameworks, middleware, or libraries in use
- If no authentication mechanisms are found, return a message that no authentication mechanisms were found and do nothing

### Endpoint Review
- Review each API endpoint one by one for authentication
- Check if authentication middleware or decorators are applied
- Verify authentication requirements are enforced
- If authentication exists, continue to the next endpoint
- If authentication does not exist, proceed to add authentication

### Add Authentication
- Apply appropriate authentication mechanisms to unprotected endpoints
- Use existing authentication framework if available
- Ensure authentication is properly integrated with the endpoint
- Verify authentication requirements are enforced

### Verification
- Verify all endpoints have appropriate authentication
- Test authentication works correctly
- Ensure no functionality is broken by authentication changes

### Implementation Checklist
- [ ] Created list of all API endpoints
- [ ] Identified authentication mechanisms in the project
- [ ] Reviewed each endpoint for authentication
- [ ] Added authentication to unprotected endpoints
- [ ] Verified authentication is properly enforced
- [ ] Tested authentication functionality
- [ ] Ensured no functionality is broken

