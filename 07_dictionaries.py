# Dictionaries
# ---------------------------------------------------------
# Dictionaries like lists are mutuable
# Dictionaries have no order unlike lists
my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age':5 }

# Accesing
print(my_cat['size'])

# Methods
print(list(my_cat.keys()))
print(list(my_cat.values()))
print(list(my_cat.items()))

# For loops
for key in my_cat.keys():
    print(key)

for value in my_cat.values():
    print(value)

for key, value in my_cat.items():
    print(key + ' : ' + str(value))

for element in my_cat.items():
    print(element)

# Comprobations
print('fat' in my_cat.values()) # check values
print('size' in my_cat) # check keys
print(my_cat.get('age',0)) # returns the age, if it doesnt exist returns 0
my_cat.setdefault('weight',10) # creates a pair if weight doesn't exist in dict

# Short program that counts the characters in a string
message = 'It was a bright cold day in April, and the clocks were striking thriteen'
count = {} # {letter, number of times that appears in the text}

for char in message.upper():
    count.setdefault(char,0)
    count[char] += 1

print(count)

# Pretty print of the dictionary
import pprint
pprint.pprint(count)
result = pprint.pformat(count) # returns the output of the pprint function
print('output: ' + result)
