#!/usr/bin/env python3
"""
Main entry point for Secure Flow CLI
Can be run directly: python main.py
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import cli as a package
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import and run the main function
from cli.cli import main

if __name__ == '__main__':
    sys.exit(main())

