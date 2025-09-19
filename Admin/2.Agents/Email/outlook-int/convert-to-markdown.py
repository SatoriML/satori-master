#!/usr/bin/env python3
"""
Outlook Email to Obsidian Markdown Converter
Converts JSON email data from AppleScript to Obsidian-compatible markdown files
"""

import json
import sys
import os
import re
from datetime import datetime
from pathlib import Path
import hashlib

class EmailToMarkdown:
    def __init__(self, vault_path=None):
        """Initialize converter with Obsidian vault path"""
        if vault_path:
            self.vault_path = Path(vault_path)
        else:
            # Default to current directory structure
            self.vault_path = Path(__file__).parent
        
        # Create directory structure
        self.inbox_path = self.vault_path / "Inbox"
        self.processed_path = self.vault_path / "Processed"
        self.archive_path = self.vault_path / "Archive"
        
        # Create directories if they don't exist
        for path in [self.inbox_path, self.processed_path, self.archive_path]:
            path.mkdir(parents=True, exist_ok=True)
        
        # Track processed emails to avoid duplicates
        self.processed_ids_file = self.vault_path / ".processed_emails"
        self.processed_ids = self.load_processed_ids()
    
    def load_processed_ids(self):
        """Load list of already processed email IDs"""
        if self.processed_ids_file.exists():
            with open(self.processed_ids_file, 'r') as f:
                return set(line.strip() for line in f)
        return set()
    
    def save_processed_id(self, email_id):
        """Save processed email ID to avoid duplicates"""
        self.processed_ids.add(email_id)
        with open(self.processed_ids_file, 'a') as f:
            f.write(f"{email_id}\n")
    
    def clean_filename(self, text, max_length=50):
        """Create safe filename from text"""
        # Remove special characters
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        # Truncate to max length
        if len(text) > max_length:
            text = text[:max_length].rsplit('-', 1)[0]
        return text.strip('-')
    
    def extract_customer(self, email_data):
        """Try to match email to existing customer"""
        sender = email_data.get('sender', '').lower()
        sender_name = email_data.get('senderName', '')
        
        # Known customer domains mapping
        customer_domains = {
            'kss.se': 'KSS',
            'svenskamoten.se': 'Svenska-Möten',
            'kvadrat.se': 'Kvadrat',
            'bilda.nu': 'Studieförbundet-Bilda',
            'vuxenskolan.se': 'Studieförbund-Vuxenskolan',
            'volleyball.se': 'Svenska-Volleybollförbundet',
            'berattarministeriet.se': 'Berättarministeriet',
            'maklarsamfundet.se': 'Mäklarsamfundet',
            'swede-electronics.se': 'Swede-Electronics',
            'rollingmill.se': 'Rolling-Mill-Service',
            'aenigma.se': 'Aenigma',
            'edvinlarssons.se': 'Edvin-Larssons',
            'jmwbygg.se': 'Jmw-Bygg',
            'ragsveden.se': 'Rågsveden-Sweden',
            'sok.se': 'SVERIGES-OLYMPISKA',
            'rf.se': 'SVERIGES-OLYMPISKA'
        }
        
        # Check domain
        for domain, customer in customer_domains.items():
            if domain in sender:
                return customer
        
        return None
    
    def format_email_body(self, body):
        """Format email body for markdown"""
        if not body:
            return ""
        
        # Convert line breaks
        body = body.replace('\\n', '\n')
        body = body.replace('\\r', '')
        body = body.replace('\\t', '  ')
        
        # Add > for email quote style
        lines = body.split('\n')
        formatted_lines = []
        
        for line in lines:
            # Detect quoted text (lines starting with >)
            if line.strip().startswith('>'):
                formatted_lines.append(line)
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def create_markdown(self, email_data):
        """Convert email JSON to markdown format"""
        # Extract data
        subject = email_data.get('subject', 'Ingen ämnesrad')
        sender = email_data.get('sender', '')
        sender_name = email_data.get('senderName', sender)
        date_str = email_data.get('date', '')
        body = email_data.get('body', '')
        has_attachments = email_data.get('hasAttachments', False)
        email_id = email_data.get('id', '')
        
        # Parse date
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d_%H%M')
            date_formatted = date_obj.strftime('%Y-%m-%d %H:%M')
            date_file = date_obj.strftime('%Y-%m-%d')
            time_file = date_obj.strftime('%H%M')
        except:
            date_formatted = date_str
            date_file = datetime.now().strftime('%Y-%m-%d')
            time_file = datetime.now().strftime('%H%M')
        
        # Try to identify customer
        customer = self.extract_customer(email_data)
        
        # Format body
        formatted_body = self.format_email_body(body)
        
        # Build markdown content
        markdown = f"""---
type: email
date: {date_formatted}
from: "{sender_name} <{sender}>"
subject: "{subject}"
{"customer: '[[" + customer + "]]'" if customer else "customer: "}
status: unread
priority: normal
has_attachments: {str(has_attachments).lower()}
email_id: "{email_id}"
---

# {subject}

**Från:** {sender_name}  
**Email:** {sender}  
**Datum:** {date_formatted}  
{"**Kund:** [[" + customer + "]]" if customer else ""}

---

## Innehåll

{formatted_body}

---

## Actions
- [ ] Läs och bedöm prioritet
- [ ] Svara om nödvändigt
- [ ] Arkivera eller ta action

## Anteckningar
*Dina anteckningar här*

---
*Email importerad: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
        
        return markdown, date_file, time_file
    
    def save_email(self, email_data):
        """Save email as markdown file"""
        email_id = email_data.get('id', '')
        
        # Skip if already processed
        if email_id in self.processed_ids:
            print(f"Skipping duplicate: {email_data.get('subject', 'Unknown')}")
            return None
        
        # Create markdown
        markdown, date_file, time_file = self.create_markdown(email_data)
        
        # Create date-based folder
        date_folder = self.inbox_path / date_file
        date_folder.mkdir(exist_ok=True)
        
        # Generate filename
        subject_clean = self.clean_filename(email_data.get('subject', 'no-subject'))
        filename = f"{time_file}-{subject_clean}.md"
        filepath = date_folder / filename
        
        # Handle duplicates by adding number
        counter = 1
        while filepath.exists():
            filename = f"{time_file}-{subject_clean}-{counter}.md"
            filepath = date_folder / filename
            counter += 1
        
        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        # Mark as processed
        self.save_processed_id(email_id)
        
        return filepath
    
    def process_json_file(self, json_file):
        """Process JSON file from AppleScript"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                emails = json.load(f)
            
            if not isinstance(emails, list):
                emails = [emails]
            
            processed_count = 0
            skipped_count = 0
            
            for email_data in emails:
                filepath = self.save_email(email_data)
                if filepath:
                    processed_count += 1
                    print(f"✓ Saved: {filepath.name}")
                else:
                    skipped_count += 1
            
            # Clean up temp file
            os.remove(json_file)
            
            print(f"\n📧 Summary:")
            print(f"  - Processed: {processed_count} emails")
            print(f"  - Skipped (duplicates): {skipped_count} emails")
            print(f"  - Location: {self.inbox_path}")
            
            return processed_count
            
        except Exception as e:
            print(f"❌ Error processing {json_file}: {e}")
            return 0

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python3 convert-to-markdown.py <json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    if not os.path.exists(json_file):
        print(f"❌ File not found: {json_file}")
        sys.exit(1)
    
    converter = EmailToMarkdown()
    converter.process_json_file(json_file)

if __name__ == "__main__":
    main()