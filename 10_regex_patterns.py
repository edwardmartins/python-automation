import re

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