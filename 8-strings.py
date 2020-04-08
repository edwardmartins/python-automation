# Symbols to write particular chacarcters in a string
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