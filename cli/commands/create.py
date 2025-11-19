"""
Create command - Create a new rule with LLM assistance
"""
import re
import sys
from pathlib import Path
from typing import List, Optional

from ..core.config import CURSOR_COMMANDS_DIR, RULES_DIR
from ..core.llm_client import LLMClient


def _extract_rule_title(rule_content: str) -> str:
    """Extract the rule title from rule content"""
    # Remove markdown code block wrapper if present
    content = rule_content
    if content.startswith('```markdown'):
        content = re.sub(r'^```markdown\n', '', content)
        content = re.sub(r'\n```\s*$', '', content)
    
    # Look for H1 heading (# Title)
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
        # Remove "Rule ID:" prefix if present
        title = re.sub(r'^Rule ID:\s*', '', title, flags=re.IGNORECASE)
        # If it's still a rule_id format, convert to title case
        if title.startswith('secure-flow-'):
            title = title.replace('secure-flow-', '').replace('-', ' ').replace('_', ' ').title()
        elif '-' in title or '_' in title:
            # Convert kebab-case or snake_case to Title Case
            title = title.replace('-', ' ').replace('_', ' ').title()
        if title:
            return title
    
    # Look for H2 heading (## Title)
    h2_match = re.search(r'^##\s+(.+)$', content, re.MULTILINE)
    if h2_match:
        return h2_match.group(1).strip()
    
    # Fallback: look for rule_id
    rule_id_match = re.search(r'rule_id:\s*secure-flow-([^\s\n]+)', content, re.IGNORECASE)
    if rule_id_match:
        # Convert kebab-case to Title Case
        title = rule_id_match.group(1).replace('-', ' ').replace('_', ' ').title()
        return title
    
    return "Rule"


def _extract_overview(rule_content: str) -> str:
    """Extract overview/description from rule content"""
    # Remove markdown code block wrapper if present
    content = rule_content
    if content.startswith('```markdown'):
        content = re.sub(r'^```markdown\n', '', content)
        content = re.sub(r'\n```\s*$', '', content)
    
    # Look for description in frontmatter
    desc_match = re.search(r'description:\s*(.+?)(?:\n|$)', content, re.IGNORECASE | re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1).strip().strip('"\'')
        if desc:
            return desc
    
    # Look for description section after frontmatter
    desc_section = re.search(r'##\s+Description\s*\n\n(.+?)(?=\n##|\n###|$)', content, re.DOTALL | re.IGNORECASE)
    if desc_section:
        desc_text = desc_section.group(1).strip()
        # Take first paragraph only
        first_para = desc_text.split('\n\n')[0] if '\n\n' in desc_text else desc_text
        # Remove code blocks
        first_para = re.sub(r'```[^`]*```', '', first_para)
        if first_para.strip():
            return first_para.strip()
    
    # Fallback: first paragraph after title
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('##') and i + 1 < len(lines):
            # Get next non-empty line
            for j in range(i + 1, len(lines)):
                if lines[j].strip() and not lines[j].startswith('#') and not lines[j].startswith('```'):
                    para = lines[j].strip()
                    # Remove code blocks
                    para = re.sub(r'```[^`]*```', '', para)
                    if para:
                        return para
    
    return "Security rule for Secure Flow framework."


def _extract_steps(rule_content: str) -> List[str]:
    """Extract steps from rule content"""
    # Remove markdown code block wrapper if present
    content = rule_content
    if content.startswith('```markdown'):
        content = re.sub(r'^```markdown\n', '', content)
        content = re.sub(r'\n```\s*$', '', content)
    
    steps = []
    
    # First, try to find Implementation section
    impl_match = re.search(r'##\s+Implementation[^\n]*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if impl_match:
        impl_content = impl_match.group(1)
        # Extract all H3 sections (### Title) with their content
        sections = re.finditer(r'###\s+(.+?)\n\n(.+?)(?=\n###|\n##|\Z)', impl_content, re.DOTALL)
        for section_match in sections:
            section_title = section_match.group(1).strip()
            section_content = section_match.group(2).strip()
            
            # Remove code blocks
            section_content = re.sub(r'```[^`]*```', '', section_content)
            
            # Check if there are H4 subsections (allow single or double newline after title)
            h4_subsections = list(re.finditer(r'####\s+(.+?)\n\n?(.+?)(?=\n####|\n###|\n##|\Z)', section_content, re.DOTALL))
            
            if h4_subsections:
                # Process each H4 subsection
                for h4_match in h4_subsections:
                    h4_title = h4_match.group(1).strip()
                    h4_content = h4_match.group(2).strip()
                    # Remove code blocks
                    h4_content = re.sub(r'```[^`]*```', '', h4_content)
                    # Get first paragraph (up to first double newline or first sentence)
                    first_para = h4_content.split('\n\n')[0] if '\n\n' in h4_content else h4_content
                    first_para = first_para.split('\n')[0].strip()  # First line
                    if first_para and len(first_para) > 10:  # Ensure meaningful content
                        steps.append(f"**{section_title} - {h4_title}**\n    - {first_para}")
            else:
                # No H4 subsections, check if there are bullet points
                bullets = re.findall(r'(?:[-*]|\d+\.)\s+(.+?)(?=\n(?:[-*]|\d+\.)|$)', section_content, re.DOTALL)
                if bullets:
                    # Extract ALL bullet points from this section
                    for bullet in bullets:
                        bullet_text = bullet.strip().split('\n')[0]  # Get first line only
                        if bullet_text and len(bullet_text) > 5:
                            steps.append(f"**{section_title}**\n    - {bullet_text}")
                else:
                    # No bullets, use the main section content as paragraph
                    first_para = section_content.split('\n\n')[0] if '\n\n' in section_content else section_content
                    first_para = first_para.split('\n')[0].strip()  # First line
                    if first_para and len(first_para) > 10:  # Ensure meaningful content
                        steps.append(f"**{section_title}**\n    - {first_para}")
    
    # If no Implementation section or no steps found, look for any H3 sections in the document
    if not steps:
        # Find all H3 sections (including those that might have H4 subsections)
        # Match from H3 to next H3, H2, or end
        h3_pattern = r'###\s+(.+?)\n\n?(.+?)(?=\n###|\n##\s+(?:Checklist|Implementation)|\Z)'
        sections = re.finditer(h3_pattern, content, re.DOTALL)
        
        for section_match in sections:
            section_title = section_match.group(1).strip()
            section_content = section_match.group(2).strip() if section_match.group(2) else ""
            
            # Skip if it's a checklist section
            if 'checklist' in section_title.lower():
                continue
            
            # Remove code blocks
            section_content = re.sub(r'```[^`]*```', '', section_content)
            
            # Check for H4 subsections first (they might come immediately after H3)
            # Allow single or double newline after H4 title
            h4_subsections = list(re.finditer(r'####\s+(.+?)\n\n?(.+?)(?=\n####|\n###|\n##|\Z)', section_content, re.DOTALL))
            
            if h4_subsections:
                for h4_match in h4_subsections:
                    h4_title = h4_match.group(1).strip()
                    h4_content = h4_match.group(2).strip()
                    h4_content = re.sub(r'```[^`]*```', '', h4_content)
                    first_para = h4_content.split('\n\n')[0] if '\n\n' in h4_content else h4_content
                    first_para = first_para.split('\n')[0].strip()
                    if first_para and len(first_para) > 10:
                        steps.append(f"**{section_title} - {h4_title}**\n    - {first_para}")
            elif section_content.strip():
                # No H4 subsections, check if there are bullet points
                bullets = re.findall(r'(?:[-*]|\d+\.)\s+(.+?)(?=\n(?:[-*]|\d+\.)|$)', section_content, re.DOTALL)
                if bullets:
                    # Extract ALL bullet points from this section
                    for bullet in bullets:
                        bullet_text = bullet.strip().split('\n')[0]  # Get first line only
                        if bullet_text and len(bullet_text) > 5:
                            steps.append(f"**{section_title}**\n    - {bullet_text}")
                else:
                    # No bullets, use the main section content as paragraph
                    first_para = section_content.split('\n\n')[0] if '\n\n' in section_content else section_content
                    first_para = first_para.split('\n')[0].strip()
                    if first_para and len(first_para) > 10:
                        steps.append(f"**{section_title}**\n    - {first_para}")
    
    # If still no steps, look for sections with bullet points (extract ALL bullets)
    if not steps:
        sections = re.finditer(r'###\s+(.+?)\n\n((?:[-*]|\d+\.)\s+.+?)(?=\n###|\n##|\Z)', content, re.DOTALL)
        for section_match in sections:
            section_title = section_match.group(1).strip()
            section_content = section_match.group(2).strip()
            section_content = re.sub(r'```[^`]*```', '', section_content)
            
            # Extract ALL bullet points from this section
            bullets = re.findall(r'(?:[-*]|\d+\.)\s+(.+?)(?=\n(?:[-*]|\d+\.)|$)', section_content, re.DOTALL)
            for bullet in bullets:
                bullet_text = bullet.strip().split('\n')[0]  # Get first line only
                if bullet_text and len(bullet_text) > 5:  # Minimum length check
                    steps.append(f"**{section_title}**\n    - {bullet_text}")
    
    return steps[:20]  # Limit to 20 steps


def _extract_checklist(rule_content: str) -> List[str]:
    """Extract checklist items from rule content"""
    # Remove markdown code block wrapper if present
    content = rule_content
    if content.startswith('```markdown'):
        content = re.sub(r'^```markdown\n', '', content)
        content = re.sub(r'\n```\s*$', '', content)
    
    checklist = []
    
    # Look for Implementation Checklist or Checklist section
    # Match from the heading to the next ## heading or end of content
    checklist_match = re.search(r'##\s+(?:Implementation\s+)?Checklist[^\n]*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if checklist_match:
        checklist_text = checklist_match.group(1)
        # Extract all checklist items (handle multiline items)
        items = re.findall(r'[-*]\s+\[[ x]\]\s+(.+?)(?=\n[-*]\s+\[|$)', checklist_text, re.DOTALL | re.MULTILINE)
        for item in items:
            # Clean up the item - take first line, remove extra whitespace
            item_clean = item.strip().split('\n')[0].strip()
            if item_clean:
                checklist.append(item_clean)
    
    return checklist


def _generate_cursor_command(rule_content: str, rule_name: str) -> str:
    """Generate a cursor command file from rule content"""
    title = _extract_rule_title(rule_content)
    overview = _extract_overview(rule_content)
    steps = _extract_steps(rule_content)
    checklist = _extract_checklist(rule_content)
    
    # Build cursor command content
    lines = [f"# {title}", "", "## Overview", "", overview, ""]
    
    if steps:
        lines.append("## Steps")
        lines.append("")
        for i, step in enumerate(steps, 1):
            lines.append(f"{i}. {step}")
            lines.append("")
    
    if checklist:
        # Format checklist title
        checklist_title = title.replace("# ", "") + " Checklist"
        lines.append(f"## {checklist_title}")
        lines.append("")
        for item in checklist:
            lines.append(f"- [ ] {item}")
    
    return "\n".join(lines)


def create_rule(
    rule_name: str,
    description: str,
    files: List[str],
    llm_token: Optional[str],
    provider: str,
    languages: List[str],
    output: Optional[str]
) -> int:
    """Create a new rule with LLM assistance using codebase context"""
    
    # Read file contents
    files_content = {}
    if files:
        for filepath in files:
            file_path = Path(filepath)
            if not file_path.exists():
                print(f"Warning: File not found: {filepath}", file=sys.stderr)
                continue
            
            try:
                content = file_path.read_text()
                files_content[str(file_path)] = content
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
    
    if not files_content:
        print("No valid files provided. Creating rule without codebase context.", file=sys.stderr)
    
    # Generate rule with LLM
    try:
        print(f"Generating rule '{rule_name}' using {provider}...")
        llm = LLMClient(provider=provider, api_key=llm_token)
        rule_content = llm.generate_rule(
            rule_name=rule_name,
            description=description,
            files_content=files_content,
            languages=languages
        )
    except Exception as e:
        print(f"Error generating rule: {e}", file=sys.stderr)
        return 1
    
    # Determine output path
    if not output:
        rule_id = f"secure-flow-{rule_name.lower().replace(' ', '-').replace('_', '-')}"
        output_path = RULES_DIR / f"{rule_id}.md"
    else:
        output_path = Path(output)
    
    # Ensure rules directory exists
    RULES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Write rule file
    try:
        output_path.write_text(rule_content)
        print(f"✅ Rule created successfully: {output_path}")
    except Exception as e:
        print(f"Error writing rule file: {e}", file=sys.stderr)
        return 1
    
    # Generate and write cursor command file
    try:
        # Determine cursor command filename - use the same name as the rule file that was created
        # Keep the "secure-flow-" prefix to match the rule file
        rule_filename = output_path.stem  # Get filename without extension
        cursor_command_name = rule_filename  # Use the same name as the rule file
        
        cursor_command_path = CURSOR_COMMANDS_DIR / f"{cursor_command_name}.md"
        
        # Ensure cursor commands directory exists
        CURSOR_COMMANDS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Generate cursor command content
        cursor_command_content = _generate_cursor_command(rule_content, rule_name)
        
        # Write cursor command file
        cursor_command_path.write_text(cursor_command_content)
        print(f"✅ Cursor command created successfully: {cursor_command_path}")
        return 0
    except Exception as e:
        print(f"Warning: Error creating cursor command file: {e}", file=sys.stderr)
        # Don't fail the whole operation if cursor command creation fails
        return 0

