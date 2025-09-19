# 📧 Outlook → Obsidian Email Sync Setup

## ✅ What This Does
Automatically fetches your Outlook emails 3 times daily (8am, 1pm, 6pm) and converts them to markdown files in your Obsidian vault.

## 🚀 Quick Setup (5 minutes)

### Step 1: Make Scripts Executable
```bash
cd "/Users/satori./Library/Mobile Documents/iCloud~md~obsidian/Documents/satori./Agent/Email/outlook-int"
chmod +x outlook-to-obsidian.applescript
chmod +x convert-to-markdown.py
```

### Step 2: Test The System
Run manually first to ensure it works:
```bash
osascript outlook-to-obsidian.applescript
```

You should see:
- Emails exported from Outlook
- New markdown files in `Inbox/` folder
- Summary of processed emails

### Step 3: Enable Automatic Runs
Install the scheduler:
```bash
# Copy plist to LaunchAgents
cp com.satori.outlook-sync.plist ~/Library/LaunchAgents/

# Load the schedule
launchctl load ~/Library/LaunchAgents/com.satori.outlook-sync.plist
```

### Step 4: Grant Permissions
When first run, macOS will ask for permissions:
1. **Allow Terminal/Script Editor** to control Outlook
2. **Allow file access** to your Obsidian vault

## 📁 Folder Structure Created

```
Agent/Email/outlook-int/
├── Inbox/              # New emails land here
│   ├── 2024-12-19/    # Daily folders
│   │   ├── 0800-Meeting-Notes.md
│   │   └── 1345-Customer-Query.md
├── Processed/          # Move completed emails here
├── Archive/            # Old emails storage
└── temp/               # Temporary JSON files
```

## 🎯 How It Works

1. **AppleScript** reads emails from your local Outlook client
2. **Python script** converts them to markdown with metadata
3. **Automatic linking** to your existing customers in `Kunder/`
4. **Duplicate detection** prevents re-importing same emails
5. **Runs 3x daily** at 8am, 1pm, and 6pm

## 📝 Email Format Example

```markdown
---
type: email
date: 2024-12-19 14:30
from: "Johan Andersson <johan@kss.se>"
subject: "Q1 Planning Meeting"
customer: [[KSS]]
status: unread
---

# Q1 Planning Meeting

**Från:** Johan Andersson
**Datum:** 2024-12-19 14:30
**Kund:** [[KSS]]

---

## Innehåll
[Email content here]

## Actions
- [ ] Review and respond
- [ ] Schedule meeting
```

## 🛠 Manual Commands

### Run Now (Manual Fetch)
```bash
osascript "/Users/satori./Library/Mobile Documents/iCloud~md~obsidian/Documents/satori./Agent/Email/outlook-int/outlook-to-obsidian.applescript"
```

### Check Schedule Status
```bash
launchctl list | grep outlook-sync
```

### Stop Automatic Runs
```bash
launchctl unload ~/Library/LaunchAgents/com.satori.outlook-sync.plist
```

### Restart Automatic Runs
```bash
launchctl unload ~/Library/LaunchAgents/com.satori.outlook-sync.plist
launchctl load ~/Library/LaunchAgents/com.satori.outlook-sync.plist
```

### View Logs
```bash
# See last run output
cat /tmp/outlook-sync.log

# Check for errors
cat /tmp/outlook-sync-error.log
```

## 🔧 Customization

### Change Schedule Times
Edit `com.satori.outlook-sync.plist` and modify the `StartCalendarInterval` section.

### Add More Customer Mappings
Edit `convert-to-markdown.py` line 64-82 to add your customer domain mappings.

### Change Email Folder
By default fetches from Inbox. To change, edit line 19 in `outlook-to-obsidian.applescript`:
```applescript
set inboxMessages to messages of [folder_name]
```

## ❓ Troubleshooting

### "Permission Denied" Error
```bash
chmod +x outlook-to-obsidian.applescript
chmod +x convert-to-markdown.py
```

### Outlook Not Found
- Ensure Microsoft Outlook is installed
- Open Outlook at least once before running

### No Emails Imported
- Check Outlook has emails from last 8 hours
- Run manually to see error messages
- Check `/tmp/outlook-sync-error.log`

### Python Error
Ensure Python 3 is installed:
```bash
python3 --version
```

## 🎉 You're Done!
Your emails will now automatically sync to Obsidian 3 times daily.
First sync will happen at the next scheduled time (8am, 1pm, or 6pm).