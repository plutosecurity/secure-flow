# Harden Dockerfile for FIPS Compliance

## Overview

Transform your Docker images to FIPS compliant by removing root users and ensuring security best practices. Make all production docker images in this repository FIPS compliant by hardening Dockerfiles and ensuring they do not run as root users.

## Steps

1. **FIPS Compliance Requirements Understanding**
    - FIPS-validated cryptographic modules: Use cryptographic libraries validated by NIST under CMVP
    - FIPS-enabled base OS: Start with base images that support FIPS mode:
        - Red Hat Enterprise Linux (RHEL) with FIPS mode enabled
        - Ubuntu Pro FIPS images
        - CentOS Stream with FIPS modules
        - SUSE Linux Enterprise with FIPS certification
    - FIPS-compliant OpenSSL: Use OpenSSL compiled with FIPS support
    - Kernel configuration: Enable FIPS mode in Linux kernel with fips=1 boot parameter

2. **Base Image Selection**
    - Use certified base images appropriate for the Dockerfile
    - Examples:
        - `FROM registry.redhat.io/ubi8/ubi:latest`
        - `FROM ubuntu:20.04-fips`
    - Use the most appropriate OS base image for each Dockerfile

3. **FIPS Module Installation**
    - Install FIPS modules:
        - For RHEL/UBI: `RUN yum install -y dracut-fips openssl`
        - Run dracut: `RUN dracut -f`

4. **FIPS Mode Configuration**
    - Configure FIPS mode: `RUN fips-mode-setup --enable`
    - Verify compliance: `RUN cat /proc/sys/crypto/fips_enabled` (should return 1)

5. **Security Hardening**
    - Remove root user execution
    - Create non-root user for application execution
    - Apply security best practices to Dockerfiles
    - Ensure all production images are hardened

6. **Verification**
    - Build containers using podman to verify builds work correctly
    - Verify FIPS mode is enabled
    - Test that applications run correctly with non-root user
    - Ensure all production docker images are FIPS compliant

## Harden Dockerfile for FIPS Compliance Checklist

- [ ] Identified all production Dockerfiles in repository
- [ ] Selected appropriate FIPS-enabled base images
- [ ] Installed FIPS modules in Dockerfiles
- [ ] Configured FIPS mode in Dockerfiles
- [ ] Removed root user execution
- [ ] Created non-root users for application execution
- [ ] Applied security best practices
- [ ] Built containers using podman to verify builds
- [ ] Verified FIPS mode is enabled
- [ ] Tested applications run correctly
- [ ] Ensured all production images are FIPS compliant

