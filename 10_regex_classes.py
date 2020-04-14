# Character classes
# --------------------------------------------------------
# \d =>  is a digit
# \D =>  is not a digit
# \w =>  is a letter or a digit
# \W =>  is not a letter and not a digit
# \s =>  is a space or a tab
# \S =>  is not a space and not a tab
import re

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
