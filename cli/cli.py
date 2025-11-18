#!/usr/bin/env python3
"""
Secure Flow CLI - Manage and execute security rules
Main entry point using argparse
"""
import argparse
import sys

from .commands import list_rules, create_rule, validate_rules, run_rule


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Secure Flow CLI - Manage and execute security rules",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all existing rules')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new rule with LLM assistance')
    create_parser.add_argument('rule_name', help='Name of the rule to create')
    create_parser.add_argument(
        '-d', '--description',
        required=True,
        help='Description of the rule'
    )
    create_parser.add_argument(
        '-f', '--files',
        action='append',
        default=[],
        help='Specific files to include as context (can be used multiple times)'
    )
    create_parser.add_argument(
        '-t', '--llm-token',
        help='LLM API token (or set ANTHROPIC_API_KEY/OPENAI_API_KEY env var)'
    )
    create_parser.add_argument(
        '-p', '--provider',
        default='anthropic',
        choices=['anthropic', 'openai'],
        help='LLM provider (default: anthropic)'
    )
    create_parser.add_argument(
        '-l', '--languages',
        action='append',
        help='Target languages (can be used multiple times, default: python, javascript, typescript)'
    )
    create_parser.add_argument(
        '-o', '--output',
        help='Output file path (default: auto-generated from rule_name)'
    )
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate all rule files')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Run a specific rule manually with LLM assistance')
    run_parser.add_argument('rule_id', help='ID of the rule to run')
    run_parser.add_argument(
        '-f', '--files',
        action='append',
        default=[],
        help='Specific files to include as context (can be used multiple times)'
    )
    run_parser.add_argument(
        '-t', '--llm-token',
        help='LLM API token (or set ANTHROPIC_API_KEY/OPENAI_API_KEY env var)'
    )
    run_parser.add_argument(
        '-p', '--provider',
        default='anthropic',
        choices=['anthropic', 'openai'],
        help='LLM provider (default: anthropic)'
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Route to appropriate command handler
    if args.command == 'list':
        return list_rules()
    elif args.command == 'create':
        # Set default languages if none provided
        languages = args.languages if args.languages else ['python', 'javascript', 'typescript']
        return create_rule(
            rule_name=args.rule_name,
            description=args.description,
            files=args.files,
            llm_token=args.llm_token,
            provider=args.provider,
            languages=languages,
            output=args.output
        )
    elif args.command == 'validate':
        return validate_rules()
    elif args.command == 'run':
        return run_rule(
            rule_id=args.rule_id,
            files=args.files,
            llm_token=args.llm_token,
            provider=args.provider
        )
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
