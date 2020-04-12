# Lists
# ---------------------------------------------------------
spam = ['car', 'bat', 'rat', 'elephant']
print(spam)
print('----------------------------------')
print(spam[0]) # first item
print(spam[-1]) # last item
print(spam[1:3]) # slice between second and thrid item
print(spam[:2]) # slice between first and second item
print(spam[1:]) # slice between second and last item
print(spam[:-1]) # slice between first and second last item
print(spam[::-1]) # inverse the list
print('car' in spam)
print('car' not in spam)

# For loop (index and value)
supplies = ['pens', 'staplers', 'throwers', 'blinders']
for i in range(len(supplies)):
    print(str(i) + ' : ' + supplies[i])

# For loop (index and value)
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# For loop (value)
for item in supplies:
    print(item)

# Multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size + ',' + color + ',' + disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size + ',' + color + ',' + disposition)

a = 'AAA'
b = 'BBB'
a, b = b, a
print(a + ',' +  b)

# List methods
spam = ['bat', 'rat', 'elephant']

# Index of the first time the value is found in the list
print(spam.index('bat')) 

# Add a value to the end of the list
spam.append('dog') 
print(spam)

# Insert a value in a particular position in the list
spam.insert(1,'chicken') 
print(spam)

# Removes an specific value in the list
spam.remove('bat') 
del spam[2]
print(spam) 

# Sorts a list
spam = [2, 5, 3.14, 1, -7]
spam.sort() 
print(spam)

# Reverse order
spam.sort(reverse=True) 
print(spam)

# Not true alphabetical order
spam = ['bat', 'Rat', 'elephant', 'ant']
spam.sort() 
print(spam)

# True alphabetical order
spam.sort(key=str.lower) 
print(spam)

# There are mutuable and inmutable datatypes
# Mutable datatypes stores references 
# Lists are mutable, tuples and strings are unmutable
# To modidy a string you have to create a new string
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]
print(new_name)

# Copies the whole list and creates a new reference
import copy
spam = ['a', 'b','c','d']
spam_copy = copy.deepcopy(spam) 
spam_copy[0] = 'z'
print(spam)
print(spam_copy)