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
names_regex = re.compile(r'Agent (\w)\w*') # group 1 -> A and B
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
