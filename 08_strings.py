# Strings basics
# --------------------------------------------------------
# Symbols to write particular characters in a string
text = 'That is Alice\'s cat \
    \n and this is a new line \
    \t and this is a tab'
print(text)

# Raw strings begins with lower case 'r' 
# The '\' character is not being ignored in raw strings
# This is very useful in regular expressions
print(r'That is Alice\'s cat')

# Multiline string
text =  """Dear Alice.
Eve's cat has been arrested for catnapping, cat buglary,
and extorsion"""
print(text)

# Strings uses indexes and slices like lists do
# Each character in a string is like and item in a list
print(text[0])
print(text[0:10])
print('ALICE' in text.upper())

# Strings methods
# --------------------------------------------------------
# Strings are unmutable so we can't modified them 
# but we can stored them in a new value
spam = 'Hello World'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

print('hello'.islower()) # all letters are lowercase
print('HELLO'.isupper()) # all letters are uppercase
print('abc'.isalpha()) # letters only
print('abc123'.isalnum()) # letters and numbers only
print('123'.isdecimal()) # numbers only
print('   '.isspace()) # whitespace only
print('Title'.istitle()) # words that begins with uppercase and continues with lowercase

# Startswith and endswith (returns bools)
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))

# Join method
print(','.join(['cats', 'rats','bats'])) # combines all strings
print(' '.join(['cats', 'rats','bats'])) 
print('\n\n'.join(['cats', 'rats','bats'])) 

# Split method
print('My name is Simon'.split()) # oposite of join
print('My name is Simon'.split('m')) 

# Ljust, rjust (left justify and right justify) and center
print('Hello'.rjust(20,'*')) 
print('Hello'.ljust(20,'*')) 
print('Hello'.center(20,'*')) 

# Strip, rstrip, lstrip (removes white spaces or any character)
print('     x      '.strip()) 
print('     x      '.lstrip()) 
print('     x      '.rstrip()) 

# Replace
spam = 'Hello there'
print(spam.replace('e', 'XYZ')) # replace every e with XYZ

# Pyperclip module (copy and paste functions that works with the computer clipboard)
import pyperclip
pyperclip.copy('Heloooooo!!!!')
print(pyperclip.paste())

# String formatting to make the code more readable (%s are conversion specifiers) 
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

print('Hello %s, you are invited to a party at %s at %s. Please bring %s.'
    % (name, place, time, food))