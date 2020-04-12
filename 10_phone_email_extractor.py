#!/usr/bin/python3
import re, pyperclip

# Regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000
( # group for everything to extract the full phone number

((\d{3})|(\(\d{3}\)))?      # area code (optional)
(\s|-)                      # first separator
(\d{3})                     # first 3 digits
-                           # separator
(\d{4})                     # last 4 digits

)                
'''
, re.VERBOSE)

# Regex for emails
email_regex = re.compile(r'''
# some.+_thing@something.com
(
[a-zA-z0-9.-_]+         # name part
@                       # symbol
[a-zA-z0-9.-]+          # domain name part
\.[a-zA-Z]{2,4}         # dot something
)        
'''
, re.VERBOSE)

# Get the text from the clipboard
text = pyperclip.paste()

# Extract emails and phones from the text
extracted_phones = phone_regex.findall(text)
extracted_emails = email_regex.findall(text)

# Take the full phone from the first group
temp = []
for phone in extracted_phones:
    temp.append(phone[0])
extracted_phones = temp

# Copy the extracted emails and phones to the clipboard
results = '\n'.join(extracted_phones) + '\n' + '\n'.join(extracted_emails)
pyperclip.copy(results)