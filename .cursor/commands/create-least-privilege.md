# Create Least Privilege

## Overview

Help analyze specified role, policy, or function and apply least privilege to generate minimal, secure permissions.

## Steps

1. **Permission Analysis**
    - Examine current permissions: list all granted permissions, identify resources/actions/conditions, find wildcards
    - For IAM: policies, resources, actions
    - For database: privileges, databases, tables, operations
    - For application: capabilities, dependencies, resources
2. **Minimal Permission Determination**
    - Identify required resources only (specific resources, no wildcards)
    - Required actions only (read-only if possible, specific actions)
    - Required conditions (time-bound, IP restrictions, MFA requirements)
    - Consider time-bound permissions (temporary, session-based, on-demand)
3. **Minimal Policy Generation**
    - Generate minimal policies for AWS IAM (resource-specific actions, conditions), GCP IAM (role bindings with conditions), Azure RBAC (data actions with scopes), database roles (GRANT specific privileges, row-level security policies), Kubernetes RBAC (resource-specific verbs, namespaces)
    - Include comments explaining why each permission is needed
4. **Migration Guide**
    - Provide before/after comparison
    - Explain removed permissions
    - Provide testing steps, and rollback plan
    - Test each permission, monitor for errors, gradual rollout if possible
    - Make actionable - provide actual minimal policy code, not just recommendations
    - Include comments explaining why each permission is needed
    - Show clear before/after comparisons

## Create Least Privilege Checklist

- [ ] Analyzed current permissions and identified wildcards
- [ ] Determined minimal required resources and actions
- [ ] Identified required conditions and time-bound permissions
- [ ] Generated minimal policies for applicable platform
- [ ] Added comments explaining each permission
- [ ] Provided before/after comparison
- [ ] Created testing steps and rollback plan
- [ ] Ensured gradual rollout approach
