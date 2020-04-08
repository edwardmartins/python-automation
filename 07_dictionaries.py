# Dictionaries
# ---------------------------------------------------------
# Dictionaries like lists are mutuable
# Dictionaries have no order unlike lists
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age':5 }

# Accesing
print(myCat['size'])

# Methods
print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))

# For loops
for key in myCat.keys():
    print(key)

for value in myCat.values():
    print(value)

for key, value in myCat.items():
    print(key + ' : ' + str(value))

for element in myCat.items():
    print(element)

# Comprobations
print('fat' in myCat.values()) # check values
print('size' in myCat) # check keys
print(myCat.get('age',0)) # returns the age, if it doesnt exist returns 0
myCat.setdefault('weight',10) # creates a pair if weight doesn't exist in dict

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
