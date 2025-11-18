# Secure Flow: Security Workflows for AI Coding Agents

Securing Open Source License: Apache 2.0

This project is an AI model-agnostic security framework that embeds secure-by-default practices into AI coding workflows (generation and review). It ships security workflows, translators for popular coding agents and IDEs, and validators to test workflow compliance.

## CLI Tool

Secure Flow includes a powerful command-line interface (CLI) for managing and executing security rules. The CLI allows you to list all existing rules, create new rules with LLM assistance using your codebase context, validate all rule files for proper structure, and run specific rules manually. The CLI is organized into modular components and uses argparse for a clean, developer-friendly interface. See the [CLI documentation](cli/README.md) for detailed usage instructions.

## Why Secure Flow?

AI coding agents accelerate development, but security policies often lag behind. Are your security practices keeping pace with rapid code generation?

❌ Security documentation that's outdated the moment it's written

❌ Compliance requirements that drift as standards evolve

❌ Manual security reviews that can't scale with AI-generated code

❌ Inconsistent security practices across teams and projects

❌ Security tools that require context switching and break developer flow

❌ Policies that exist in wikis but never make it into actual code

Secure Flow solves this by turning security policies into executable workflows that developers use directly in their IDE, with real-time updates from trusted sources.

## During and After Code Generation

Secure Flow is designed to integrate seamlessly across the entire AI coding lifecycle.

**Before code generation**, workflows can be used for the design of a product and for spec-driven development. You can use the workflows in the "planning phase" of an AI coding agent to steer models toward secure patterns from the start.

**During code generation**, workflows help AI agents prevent security issues as code is being written.

**After code generation**, AI agents like Cursor, GitHub Copilot, Claude Code, Windsurf, and other IDE assistants can use the workflows for code review and remediation.

## Security Coverage

Our workflows address critical security challenges across the development lifecycle:

🔐 **Cryptography & Secrets**: Post-quantum algorithms, secure key rotation, certificate pinning, secrets management

🛡️ **Vulnerability Management**: CISA KEV remediation, dependency scanning, exploit prevention, patch prioritization

🔑 **Access Control**: Multi-factor authentication, OAuth flows, session security, privilege escalation prevention

⚡ **Compliance Automation**: SOC 2, ISO 27001, HIPAA, PCI DSS validation, audit trail generation

📦 **Infrastructure Security**: Container hardening, FIPS compliance, Kubernetes security, IaC validation

☁️ **API & Service Security**: Authentication review, rate limiting, input sanitization, secure defaults

📱 **Threat Modeling**: Attack surface analysis, risk assessment, security architecture review

🔍 **Remediation & Testing**: Automated fixes, security test generation, vulnerability triage, compliance gap analysis

## Quick Start

Get started in minutes:

1. **Download the workflows** from our releases page or clone this repository
2. **Copy to your project** - Place IDE-specific workflows in your repository
3. **Start coding** - AI assistants will automatically follow security best practices

Additional details in the [Get Started](#installation) section →

## How It Works

At Pluto Security, we've been researching how this feature can go far beyond productivity - into secure development and compliance automation.

We treat `.cursor/commands` (and similar IDE workflow directories) as a **policy execution layer**: a way to define repeatable, reviewable, and context-aware actions that developers can trigger at any time.

We designed workflows for repeatable security tasks that developers can run directly in their workflow - each workflow can fetch live data from trusted internet sources (official docs, advisories, best-practice repositories) to stay always up-to-date.

### The Policy Execution Layer

Security workflows are written in unified markdown format (`sources/` directory)

Conversion tools translate workflows to IDE-specific formats (Cursor commands, Claude skills, Copilot, etc.)

Release automation packages workflows into downloadable ZIP files

AI assistants reference these workflows when generating or reviewing code

Secure code is produced automatically without developer intervention

### Real-Time Policy Updates

The best part? You can plug in your own stack:

- **Compliance SaaS platforms** (SOC 2, ISO 27001, HIPAA, CAIQ Lite)
- **Internal security documentation** or wikis
- **CLI Tools** (Snyk / Trivy / AWS CLI)
- **Scripts** (Python, Bash, or any executable)

Each workflow execution can automatically:
- Pull the most recent guidance from trusted sources (to ensure alignment with the latest policies, standards, and compliance frameworks)
- Run your own custom CLI commands
- Execute pre-made Python scripts in the right context

This means developers use simple, reusable workflows created by security teams - but those workflows evolve in real time, keeping code and compliance aligned.

## Repository Structure

```
sources/           # Source workflows (unified markdown format)
.cursor/           # Cursor IDE commands (generated, committed)
claude-skills/     # Claude Code skills (generated, committed)
src/               # Conversion and validation tools
dist/              # Other IDE bundles (generated, not committed)
```

## Installation

### Option 1: Clone the Repository

```bash
git clone https://github.com/plutosecurity/secure-flow.git
cd secure-flow
```

### Option 2: Copy Workflows into Existing Project

```bash
# For Cursor IDE
cp -r secure-flow/.cursor /path/to/your/project/

# For Claude Code
cp -r secure-flow/claude-skills /path/to/your/project/
```

### Option 3: Manual Setup

1. Create the appropriate directory in your project root:
   - `.cursor/commands/` for Cursor IDE
   - `claude-skills/` for Claude Code
   - Or other IDE-specific locations
2. Copy or author the workflow files you need

## Available Workflows

This repository includes the following security workflows:

- **`create-secure-template`** - Generate secure code templates with security best practices
- **`create-security-tests`** - Create security test cases and validation scripts
- **`create-threat-model`** - Generate threat models for applications and systems
- **`explain-ai-threats`** - Explain AI-specific security threats and mitigations
- **`gate-critical-vulns`** - Set up CI/CD checks to block critical vulnerabilities
- **`harden-dockerfile-fips`** - Make Dockerfiles FIPS compliant with security hardening
- **`fix-exploitable-vulns`** - Fix CISA Known Exploited Vulnerabilities (KEV) found in your codebase
- **`review-api-auth`** - Review and add authentication to API endpoints
- **`security-remediation`** - Scan and fix high-impact vulnerabilities in the codebase
- **`validate-compliance`** - Validate compliance with security frameworks and standards

## IDE-Specific Usage

### Cursor IDE

1. Type `/` in Cursor's AI chat or agent input
2. Select from the available security workflows
3. Let the AI execute the workflow with the relevant project context

Workflows are stored in `.cursor/commands/` as Markdown files.

### Claude Code

1. Import skills from the `claude-skills/` directory
2. Activate skills in Claude Code settings
3. Use skills during code generation and review

### Other IDEs

Workflows can be adapted for:
- GitHub Copilot
- Windsurf
- Codeium
- Other AI-powered IDEs

## For Developers

```bash
git clone https://github.com/plutosecurity/secure-flow.git && cd secure-flow

# Validate workflows
python src/validate_unified_workflows.py sources/

# Generate IDE-specific formats
python src/convert_to_ide_formats.py

# More options
python src/convert_to_ide_formats.py --help
```

Maintainers: See `CONTRIBUTING.md` for release process.

## Workflow Structure

All workflows follow a consistent format for clarity and consistency:

- **Title**: Clear workflow name as heading
- **Overview**: Brief description of the workflow's purpose
- **Steps**: Numbered steps with detailed sub-bullets
- **Checklist**: Checkbox list to track completion

## Best Practices

- **Be specific**: Describe the expected outcome and acceptance criteria
- **Provide context**: Reference security frameworks, compliance standards, or architecture
- **Set boundaries**: Clarify scope, assumptions, and tooling limits
- **Include examples**: Show expected formats or responses when helpful
- **Stay focused**: Keep each workflow targeted to a single, clear security objective
- **Review together**: Treat workflow changes like code changes and review in PRs
- **Use descriptive names**: Make filenames reflect the workflow's security purpose
- **Follow security frameworks**: Reference OWASP, NIST, CWE, or compliance standards where relevant

## Community

📋 **Issues**: Report bugs or request features

💬 **Discussions**: Join the conversation

🤝 **Contributing**: Learn how to contribute

## Licensing

This project is open source and available under the [Apache License 2.0](LICENSE).

Copyright © 2025 Pluto Security
