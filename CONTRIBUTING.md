# Contributing to Secure Flow

Thank you for your interest in contributing to Secure Flow! This document provides guidelines and instructions for contributing to the project.

## How to Contribute

We welcome contributions in many forms:

- 🐛 **Bug reports**: Report issues you've found
- 💡 **Feature requests**: Suggest new workflows or improvements
- 📝 **Documentation**: Improve existing docs or add new ones
- 🔧 **Code**: Submit pull requests for bug fixes or new features
- 🔄 **Workflows**: Add new security workflows or improve existing ones

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/secure-flow.git
   cd secure-flow
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Steps

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if applicable)
pip install -r requirements.txt

# Validate workflows
python src/validate_unified_workflows.py sources/

# Generate IDE-specific formats
python src/convert_to_ide_formats.py
```

## Workflow Development Guidelines

### Creating New Workflows

1. **Create a new markdown file** in the `sources/` directory
2. **Follow the standard workflow structure**:
   - Title (as H1 heading)
   - Overview section
   - Steps section (numbered with detailed sub-bullets)
   - Checklist section

3. **Example structure**:
   ```markdown
   # Workflow Name

   ## Overview

   Brief description of what this workflow does and why it's important.

   ## Steps

   1. **Step Title**
       - Detailed explanation
       - Sub-points and requirements
   2. **Next Step**
       - Additional instructions
       - Implementation details

   ## Workflow Name Checklist

   - [ ] Checklist item 1
   - [ ] Checklist item 2
   - [ ] Checklist item 3
   ```

### Workflow Best Practices

- **Be specific**: Describe expected outcomes and acceptance criteria
- **Provide context**: Reference security frameworks (OWASP, NIST, CWE) where relevant
- **Set boundaries**: Clarify scope, assumptions, and tooling limits
- **Include examples**: Show expected formats or responses when helpful
- **Stay focused**: Keep each workflow targeted to a single, clear security objective
- **Use descriptive names**: Make filenames reflect the workflow's security purpose

### Security Considerations

- Ensure workflows follow security best practices
- Reference authoritative sources (official docs, advisories, standards)
- Include validation steps where appropriate
- Consider edge cases and error handling

## Code Contributions

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and modular

### Testing

- Test your changes locally before submitting
- Ensure existing tests still pass
- Add tests for new functionality when applicable

### Validation

Before submitting, run:

```bash
# Validate workflow syntax and structure
python src/validate_unified_workflows.py sources/

# Generate IDE-specific formats
python src/convert_to_ide_formats.py

# Check for linting issues
# (add linting commands as they're set up)
```

## Submitting Changes

### Commit Messages

Write clear, descriptive commit messages:

```
Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain the problem and solution, not just what changed.

- Bullet points are okay too
- Use present tense ("Add feature" not "Added feature")
```

### Pull Request Process

1. **Update your branch** with the latest changes from main:
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Push your changes** to your fork:
   ```bash
   git push origin your-branch
   ```

3. **Create a Pull Request** on GitHub:
   - Provide a clear title and description
   - Reference any related issues
   - Explain what changes you made and why
   - Include screenshots or examples if applicable

4. **Respond to feedback**: Be open to suggestions and make requested changes

### Pull Request Checklist

- [ ] Code/workflows follow project guidelines
- [ ] Changes are tested and validated
- [ ] Documentation is updated if needed
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts with main branch

## Release Process

For maintainers:

1. Update version numbers
2. Update CHANGELOG.md
3. Create a release tag
4. Generate IDE-specific bundles
5. Publish release notes

## Questions?

- Open an [issue](https://github.com/plutosecurity/secure-flow/issues) for questions or discussions
- Check existing issues and discussions before creating new ones
- Be respectful and constructive in all interactions

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (Apache License 2.0).

Thank you for contributing to Secure Flow! 🎉

