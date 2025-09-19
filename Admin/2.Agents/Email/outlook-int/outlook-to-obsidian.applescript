#!/usr/bin/osascript

-- Outlook to Obsidian Email Exporter
-- Exports emails from Outlook to JSON for Python processing
-- Run 3x daily: 8am, 1pm, 6pm

on run
	set exportPath to (POSIX path of (path to home folder)) & "Library/Mobile Documents/iCloud~md~obsidian/Documents/satori./Agent/Email/outlook-int/temp/"
	set currentTime to (current date)
	set timeStamp to my formatDate(currentTime)
	
	-- Create temp directory if needed
	do shell script "mkdir -p " & quoted form of exportPath
	
	-- Get emails from last 8 hours (to cover time between runs)
	set hoursBack to 8
	set cutoffTime to currentTime - (hoursBack * hours)
	
	tell application "Microsoft Outlook"
		-- Get inbox messages
		set inboxMessages to messages of inbox whose time received > cutoffTime
		
		set emailCount to 0
		set jsonOutput to "["
		
		repeat with theMessage in inboxMessages
			set emailCount to emailCount + 1
			
			-- Extract email data
			set msgSubject to subject of theMessage as string
			set msgSender to email address of sender of theMessage as string
			set msgSenderName to name of sender of theMessage as string
			set msgBody to plain text content of theMessage as string
			set msgDate to time received of theMessage
			set msgID to id of theMessage as string
			
			-- Check if has attachments
			set hasAttachments to (count of attachments of theMessage) > 0
			
			-- Escape special characters for JSON
			set msgSubject to my escapeForJSON(msgSubject)
			set msgBody to my escapeForJSON(msgBody)
			set msgSenderName to my escapeForJSON(msgSenderName)
			
			-- Build JSON object
			set emailJSON to "{" & ¬
				"\"id\":\"" & msgID & "\"," & ¬
				"\"subject\":\"" & msgSubject & "\"," & ¬
				"\"sender\":\"" & msgSender & "\"," & ¬
				"\"senderName\":\"" & msgSenderName & "\"," & ¬
				"\"date\":\"" & my formatDate(msgDate) & "\"," & ¬
				"\"body\":\"" & msgBody & "\"," & ¬
				"\"hasAttachments\":" & hasAttachments & ¬
				"}"
			
			if emailCount > 1 then
				set jsonOutput to jsonOutput & ","
			end if
			set jsonOutput to jsonOutput & emailJSON
			
		end repeat
		
		set jsonOutput to jsonOutput & "]"
		
		-- Save to temp file
		set tempFile to exportPath & "emails_" & timeStamp & ".json"
		do shell script "echo " & quoted form of jsonOutput & " > " & quoted form of tempFile
		
		-- Mark emails as read (optional)
		repeat with theMessage in inboxMessages
			set is read of theMessage to true
		end repeat
		
	end tell
	
	-- Trigger Python converter
	do shell script "cd " & quoted form of exportPath & " && python3 ../convert-to-markdown.py " & quoted form of tempFile
	
	return "Exported " & emailCount & " emails"
end run

-- Format date for filename
on formatDate(theDate)
	set y to year of theDate
	set m to (month of theDate as integer)
	set d to day of theDate
	set h to hours of theDate
	set min to minutes of theDate
	
	-- Pad with zeros
	if m < 10 then set m to "0" & m
	if d < 10 then set d to "0" & d
	if h < 10 then set h to "0" & h
	if min < 10 then set min to "0" & min
	
	return (y as string) & "-" & m & "-" & d & "_" & h & min
end formatDate

-- Escape special characters for JSON
on escapeForJSON(str)
	set str to my findAndReplace(str, "\\", "\\\\")
	set str to my findAndReplace(str, "\"", "\\\"")
	set str to my findAndReplace(str, return, "\\n")
	set str to my findAndReplace(str, tab, "\\t")
	set str to my findAndReplace(str, character id 13, "\\r")
	return str
end escapeForJSON

-- Find and replace helper
on findAndReplace(theText, findStr, replaceStr)
	set AppleScript's text item delimiters to findStr
	set theTextItems to text items of theText
	set AppleScript's text item delimiters to replaceStr
	set theText to theTextItems as string
	set AppleScript's text item delimiters to ""
	return theText
end findAndReplace