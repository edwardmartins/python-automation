# Reading and writing files
# --------------------------------------------------------

# Open a file in Read Mode, you can't write or modify it
hello_file = open(r'C:\Users\edu\Desktop\hello.txt')
content = hello_file.read()
print(content)

# Returns the content of a file as a list of strings
hello_file = open(r'C:\Users\edu\Desktop\hello.txt')
content = hello_file.readlines()
print(content)

# Open a file in Write Mode, overwrites the existing file
hello_file = open(r'C:\Users\edu\Desktop\hello_2.txt', 'w')
hello_file.write('Hello!!!!!!!!!!!\n')
hello_file.write('Hello!!!!!!!!!!!')

# Open a file in Append Mode, appends the text to an existing file
hello_file = open(r'C:\Users\edu\Desktop\hello_2.txt', 'a')
hello_file.write('\nAppending!!!!!!!!!!!')

# Close a file
hello_file.close()

# The shelve module saves data structures and variables
# -------------------------------------------------------
import shelve

# Dictionary structure
shelf_file = shelve.open('my_data') 
shelf_file['cats'] = ['zophie', 'puka', 'simon']
shelf_file.close()

# Saves it into the program so you can read them later
shelf_file = shelve.open('my_data')
print(shelf_file['cats'])
print(list(shelf_file.keys()))
print(list(shelf_file.values()))