# Harden Configuration

## Overview

Help perform security hardening analysis and remediation of configuration files. Identify vulnerabilities and apply secure defaults.

## Steps

1. **Configuration File Discovery**
    - Identify all config files: environment files (.env), application config (settings.py, config.json), Docker files, infrastructure (terraform, kubernetes), web server (nginx.conf, apache.conf), CI/CD configs, framework-specific configs
2. **Security Vulnerability Assessment**
    - Scan for debug mode in production, weak authentication/secrets, missing HTTPS/TLS, overly permissive CORS, missing security headers, insecure cookies, hardcoded secrets, insecure file permissions, plaintext database credentials, and logging of sensitive data
3. **Implementation of Secure Defaults**
    - For each file: identify insecure settings and categorize by risk
    - Apply secure defaults (disable debug, force HTTPS, add security headers, configure CORS, set secure cookie flags, use environment variables, set file permissions)
    - Modify files directly preserving functionality
    - Add security comments explaining decisions
    - Provide change summary
4. **Framework-Specific Hardening**
    - Python: Disable DEBUG, set ALLOWED_HOSTS, secure SECRET_KEY, enable CSRF, secure sessions
    - Node.js: Set NODE_ENV=production, configure Helmet.js, secure cookies, rate limiting
    - Java: Set production profile, disable debug endpoints, security headers
    - Docker: Use non-root user, minimal images, resource limits
    - Make actual changes to configuration files, not just recommendations
    - Provide production-ready, secure configurations following industry best practices

## Harden Configuration Checklist

- [ ] Discovered all configuration files
- [ ] Assessed security vulnerabilities
- [ ] Identified insecure settings by risk
- [ ] Applied secure defaults
- [ ] Modified files preserving functionality
- [ ] Added security comments explaining decisions
- [ ] Applied framework-specific hardening
- [ ] Provided change summary
- [ ] Ensured production-ready configurations
