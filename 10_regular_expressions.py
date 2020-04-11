# Regular expressions
# --------------------------------------------------------
import re

# Find a phone number in the text
text = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line' 

# 1) We create a regex object with compile
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # looking for 3 digits(\d) and a dash

# 2) Then we create a match object

 # find one ocurrence in the text (returns a match object)
match_object = phone_num_regex.search(text)
print(match_object.group())

# find all ocurrences in the text (returns a list of strings)
match_list = phone_num_regex.findall(text) 
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

# Regex find all method
# --------------------------------------------------------

# without groups (returns a list of strings)
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
ml = phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(ml)

# with groups (returns a list of tuples of strings)
phone_regex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
ml = phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(ml)

# Character classes
# --------------------------------------------------------
# \d =>  is a digit
# \D =>  is not a digit
# \w =>  is a letter or a digit
# \W =>  is not a letter and not a digit
# \s =>  is a space or a tab
# \S =>  is not a space and not a tab

xmas_regex = re.compile(r'\d+\s\w+')
ml = xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
            swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(ml)

# Making your own character classes
# --------------------------------------------------------
# regex_obj = re.compile(r'[xyz]') => with brackets same as x|y|z

text = 'Robocop eats baby food'
# Only vowels
vowel_rege = re.compile(r'[aeiouAEIOU]') # [a|e|i|o|u]
ml = vowel_rege.findall(text)
print(ml)

# The opposite of a vowel
consonant_rege = re.compile(r'[^aeiouAEIOU]') 
ml = consonant_rege.findall(text)
print(ml)

# Only letters
only_letters_rege = re.compile(r'[a-zA-z]') 
ml = only_letters_rege.findall(text)
print(ml)

# The match has to occur at the beggining of the string^( )
begins_with = re.compile(r'^Hello')
mo = begins_with.search('Hello there')
print(mo.group())
mo = begins_with.search('He said Hello')
print(mo == None)

# The match has to occur at the end of the string $( )
ends_with = re.compile(r'world!$')
mo = ends_with.search('Hello world!')
print(mo.group())
mo = ends_with.search('world! Hello')
print(mo == None)

# The match has to be the entire string
all_digits = re.compile(r'^\d+$')
mo = all_digits.search('123456789')
print(mo.group())

# The dot (.) character match any character except the new line
at_regex = re.compile(r'.at') 
ml = at_regex.findall('The cat in the hat sat on the flat mat')
print(ml)

at_regex = re.compile(r'.{1,2}at') 
ml = at_regex.findall('The cat in the hat sat on the flat mat')
print(ml)

# (.*) means anything => take whataver you find after First Name and Last Name
# When there is groups findAll returns the groups not the entire match
text = 'First Name: Al Last Name: Sweigart'
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)') 
ml = name_regex.findall(text)
print(ml)

# (.*) uses greedy mode, so is gonna take the maximum string possible
# (.*?) non greedy mode, the minimun string possible
serve = '<To serve humans> for dinner>'
nongreedy = re.compile(r'<(.*?)>')
ml = nongreedy.findall(serve)
print(ml)

greedy = re.compile(r'<(.*)>')
ml = greedy.findall(serve)
print(ml)

# Include new line characters in (.*) expression
prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law.'
dot_star = re.compile(r'.*', re.DOTALL) 
mo = dot_star.search(prime)
print(mo.group())

# Case sensitive matching
vowel_regex_caps = re.compile(r'[aeiou]', re.IGNORECASE)
ml = vowel_regex_caps.findall('Al, why does your programming book talk about Robocop so much?')
print(ml)

# Find and replace with the sub() method
# --------------------------------------------------------
text = 'Agent Alice gave the secret documents to Agent Bob'

# Sub method not only finds, also replaces
names_regex = re.compile(r'Agent \w+')
res = names_regex.sub('REDACTED',text)
print(res)

# Sub methods replaces with groups results
names_regex = re.compile(r'Agent (\w)\w*') # group 1 -> A or B
res = names_regex.sub(r'Agent \1****',text) # \1 means use the text for group 1
print(res)

# Verbose format (let you add white space and comments)
# --------------------------------------------------------
re.compile(r'''

(\d\d\d-) |     # area code without parens
(\(\d\d\d\))    # or area code with parens   
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits

''', re.VERBOSE | re.DOTALL | re.IGNORECASE) # you can combine multiple options in the second argument
