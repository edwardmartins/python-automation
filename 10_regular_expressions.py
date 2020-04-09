# Regular expressions
# --------------------------------------------------------
# Find a phone number in the text
import re

text = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'

# Looking for 3 digits and a dash
phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d') 

# Find one ocurrence in the text
match_object = phone_number_regex.search(text) 
print(match_object.group())

# Find all ocurrences in the text
match_object = phone_number_regex.findall(text) 
print(match_object)






