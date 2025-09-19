#!/bin/bash

# Test script for Outlook to Obsidian sync
# Run this to test the system before setting up automation

echo "🚀 Testing Outlook to Obsidian Email Sync..."
echo "==========================================="
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Outlook is running
if ! pgrep -x "Microsoft Outlook" > /dev/null; then
    echo "⚠️  Microsoft Outlook is not running."
    echo "   Please start Outlook and try again."
    exit 1
fi

echo "✅ Outlook is running"
echo ""

# Make scripts executable
echo "📝 Making scripts executable..."
chmod +x outlook-to-obsidian.applescript
chmod +x convert-to-markdown.py
echo "✅ Scripts are executable"
echo ""

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p Inbox
mkdir -p Processed
mkdir -p Archive
mkdir -p temp
echo "✅ Directories created"
echo ""

# Run the AppleScript
echo "📧 Fetching emails from Outlook..."
echo "   This may take a moment..."
echo ""

# Run and capture output
output=$(osascript outlook-to-obsidian.applescript 2>&1)
exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "✅ Email fetch completed successfully!"
    echo "   $output"
    echo ""
    
    # Show imported emails
    echo "📊 Imported emails:"
    echo "==================="
    if [ -d "Inbox" ] && [ "$(ls -A Inbox)" ]; then
        find Inbox -name "*.md" -type f -exec basename {} \; | head -10
        total_count=$(find Inbox -name "*.md" -type f | wc -l | tr -d ' ')
        echo ""
        echo "Total emails in Inbox: $total_count"
    else
        echo "No emails found in Inbox/"
    fi
else
    echo "❌ Error occurred during email fetch:"
    echo "   $output"
    echo ""
    echo "Troubleshooting tips:"
    echo "1. Make sure Outlook has emails from the last 8 hours"
    echo "2. Grant permission when macOS asks to control Outlook"
    echo "3. Check that Python 3 is installed: python3 --version"
fi

echo ""
echo "==========================================="
echo "Test complete!"
echo ""
echo "Next steps:"
echo "1. If successful, check the Inbox/ folder for your emails"
echo "2. Review the markdown formatting"
echo "3. Run setup to enable automatic syncing 3x daily"