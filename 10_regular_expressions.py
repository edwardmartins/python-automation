# Regular expressions
# --------------------------------------------------------
import re

# Find a phone number in the text
text = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line' 

# 1) We create a regex object with compile
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # looking for 3 digits(\d) and a dash

# 2) Then we create a match object
match_object = phone_num_regex.search(text) # find one ocurrence in the text
print(match_object.group())

match_object = phone_num_regex.findall(text) # find all ocurrences in the text
print(match_object)

# We use parenthesis to create groups
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search(text)
print(mo.group(1))
print(mo.group(2))

# If we want to search for a parenthesis in the text we use \(and\)
phone_num_regex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phone_num_regex.search('Call me (415) 555-1011 tomorrow')
print(mo.group())

# Pipe character
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)') # looking for prefix "Bat" and any sufix in the list
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1)) # with group(1) we know what suffix we found

# Match a specific number of repetitions
# --------------------------------------------------------
# ? -> Matches a group 0 or 1 time
bat_regex = re.compile(r'Bat(wo)?man') 
mo = bat_regex.search('The adventures of Batman')
print(mo.group())
mo = bat_regex.search('The adventures of Batwoman')
print(mo.group())

# * -> = Matches a group 0 or more times
bat_regex = re.compile(r'Bat(wo)*man') 
mo = bat_regex.search('The adventures of Batwowowowowoman')
print(mo.group())

# + -> = Matches a group 1 or more times
bat_regex = re.compile(r'Bat(wo)+man')
mo = bat_regex.search('The adventures of Batwowoman')
print(mo.group())

# {x} -> Matching a specific number "x" of repetitions in a group
ha_regex = re.compile(r'(Ha){3}')
mo = ha_regex.search('He said "HaHaHa"')
print(mo.group())

# {x,y} -> Matching at least "x" of repetitions and at most "y" 
# {3,} => 3 or more  {,5} => 0 to 5
ha_regex = re.compile(r'(Ha){3,5}') 
mo = ha_regex.search('He said "HaHaHaHaHa"') 
print(mo.group())

# Match special characters like *, +, ? putting a backslash
qmark_regex = re.compile(r'\+\*\?') 
mo = qmark_regex.search('I learned about +*? regex syntax')
print(mo.group())

# Examples
# --------------------------------------------------------
# Making the area code optional in a phone number
phone_num_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') 
mo = phone_num_regex.search('Call me 415-555-1011 tomorrow')
print(mo.group())
mo = phone_num_regex.search('Call me 555-1011 tomorrow')
print(mo.group())

# Matching multiple phone numbers
phone_num_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){2}') 
mo = phone_num_regex.search('My numbers are 415-555-1011,555-1011')
print(mo.group())

# Matching 3 to 5 digits -> always matches the longest string possible
digit_regex = re.compile(r'\d{3,5}')
mo = digit_regex.search('123456789')
print(mo.group())

# Matching 3 to 5 digits -> matching the smallest string possible
digit_regex = re.compile(r'\d{3,5}?')
mo = digit_regex.search('123456789')
print(mo.group())

# Regex Character Classes
# --------------------------------------------------------








