# Regular expressions
# --------------------------------------------------------
import re

# Find a phone number in the text
text = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line' 

# 1) We create a regex object with compile
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d') # looking for 3 digits(\d) and a dash

# 2) Then we create a match object
match_object = phone_num_regex.search(text) # find one ocurrence in the text
print(match_object.group())

match_object = phone_num_regex.findall(text) # find all ocurrences in the text
print(match_object)

# We use parenthesis to create groups
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phone_num_regex.search(text)
print(mo.group(1))
print(mo.group(2))

# If we want to search for a parenthesis in the text we use \(and\)
phone_num_regex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d')
mo = phone_num_regex.search('Call me (415) 555-1011 tomorrow')
print(mo.group())

# Pipe character
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)') # looking for prefix "Bat" and any sufix in the list
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1)) # with group(1) we know what suffix we found



