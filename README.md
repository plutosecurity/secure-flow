# Cursor Secure Commands

A curated collection of Cursor slash-command prompts focused on security workflows. These commands help your team implement security best practices, validate compliance, and maintain secure code directly inside the Cursor IDE.

## What are Cursor Commands?

Cursor Commands are reusable AI prompts saved as Markdown files in
`.cursor/commands/`. When you type `/` in Cursor's chat input, the IDE lists
every command from your project and your global library so you can insert the
prompt instantly. They act like AI-driven shortcuts that automate repetitive
tasks, reinforce team standards, and keep feedback consistent.

## Features

- ** Quick access**: Type `/` to surface every command without leaving your flow
- ** Reusable**: Standardize security prompts for common tasks across the whole team
- ** Shareable**: Store commands in git so they ship with your repository
- ** Focused**: Each command targets a specific security workflow with clear structure
- ** Security-first**: Built-in security best practices and compliance validation
- ** Customizable**: Edit or extend the Markdown files to match your processes

## How commands work

Commands can live in two places:

- Project commands: Store Markdown files in `.cursor/commands` inside your repository
- Global commands: Store personal commands in `~/.cursor/commands` on your machine

Cursor automatically scans both directories when you type `/`, combines the
results, and inserts the selected command into the chat ready to run.

## How to use

1. Type `/` in Cursor's AI chat or agent input
2. Select from the available security commands
3. Let the AI execute the prompt with the relevant project context

## Creating commands

- Create a `.cursor/commands` directory in your project root
- Add `.md` files with descriptive names (for example, `fix-vuln.md`, `validate-compliance.md`)
- Write clear Markdown instructions describing what the command should accomplish
- Open Cursor, type `/`, and choose your new command to execute it immediately

Example structure:

```text
.cursor/
└── commands/
    ├── create-evidence.md
    ├── create-least-privilege.md
    ├── create-secure-template.md
    ├── create-security-tests.md
    ├── create-threat-model.md
    ├── explain-ai-threats.md
    ├── explain-risk.md
    ├── fix-vuln.md
    ├── harden-config.md
    ├── trace-secret.md
    └── validate-compliance.md
```

## Quick start

1. Clone this repository or copy the `.cursor/commands/` directory into your project
2. Open the project in Cursor IDE
3. Type `/` in the AI chat to browse available security commands
4. Select a command and let Cursor execute the prompt with your code context

## Installation options

```bash
# Option 1: clone the repository
git clone https://github.com/your-org/cursor-secure-commands.git
cd cursor-secure-commands
```

```bash
# Option 2: copy commands into an existing project
cp -r cursor-secure-commands/.cursor /path/to/your/project/
```

Alternatively, create the directory manually:

1. Create `.cursor/commands/` in your project root
2. Copy or author the Markdown command files you need

## Writing your own commands

Use the existing files as templates or start from scratch. All commands follow a consistent structure:

```bash
touch .cursor/commands/my-security-command.md
```

```markdown
# My Security Command

## Overview

Brief description of what this command does.

## Steps

1. **Step Title**
    - Detailed explanation
    - Sub-points and requirements
2. **Next Step**
    - Additional instructions
    - Implementation details

## My Security Command Checklist

- [ ] Checklist item 1
- [ ] Checklist item 2
- [ ] Checklist item 3
```

## Command Structure

All commands follow a consistent format for clarity and consistency:

- **Title**: Clear command name as heading
- **Overview**: Brief description of the command's purpose
- **Steps**: Numbered steps with detailed sub-bullets
- **Checklist**: Checkbox list to track completion

## Best practices

- **Be specific**: Describe the expected outcome and acceptance criteria
- **Provide context**: Reference security frameworks, compliance standards, or architecture
- **Set boundaries**: Clarify scope, assumptions, and tooling limits
- **Include examples**: Show expected formats or responses when helpful
- **Stay focused**: Keep each command targeted to a single, clear security objective
- **Review together**: Treat command changes like code changes and review in PRs
- **Use descriptive names**: Make filenames reflect the command's security purpose
- **Follow security frameworks**: Reference OWASP, NIST, CWE, or compliance standards where relevant

## Support

- Open an [issue](https://github.com/plutosecurity/cursor-secure-commands/issues) for feedback or requests
- Refer to this README for the command index that ships with the prompts

## License

This project is open source and available under the [MIT License](LICENSE).

