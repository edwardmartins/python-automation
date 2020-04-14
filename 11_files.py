# Files
# --------------------------------------------------------
# Slash separator en Windows(\) in Mac and Linux (/)

# If you want to have a literal slash on Windows 
# you have to put two(\\) or make a raw string 
path = 'C:\\Users\\edu\\Desktop\\Python Automation'
print(path)

path = r'C:\Users\edu\Desktop\Python Automation'
print(path)

# Library for file path compatibility between OS
import os
path = os.path.join('folder1','folder2','folder3', 'file.png')
print(path)

# Current working directory
working_directory = os.getcwd()
print(working_directory)

# Change current working directory
changed_directory  = os.chdir(r'C:\Users\edu\Desktop\Python Automation')
print(os.getcwd())

# Absolute and relative paths
# --------------------------------------------------------
# Absolute file paths (begins with the root folder)
# Gives you the complete location of the program
# C:\spam.png

# Relative file path 
# Always relative to the current working directory
# spam.png

# The (.) dot and the (..) 
# --------------------------------------------------------
# .  => current folder
# .. => the parent folder


# Functios in the OS module
# --------------------------------------------------------

# Returns the absolute path of a file 
absolute_path = os.path.abspath('01_helloworld.py')
print(absolute_path)

# Returns true if the path is an absolute path
is_absolute_path = os.path.isabs(r'C:\Users\edu\Desktop\Python Automation\01_helloworld.py')
print(is_absolute_path)

# Gives you a relative path from a file given a working directory
relative_path = os.path.relpath(r'C:\Users\edu\Desktop\Python Automation\01_helloworld.py', r'C:\Users\edu' )
print(relative_path)

# Returns the directory part of a path
directory_path = os.path.dirname(r'C:\Users\edu\Desktop\Python Automation\01_helloworld.py')
print(directory_path)

# Returns the last part of the path
base_path = os.path.basename(r'C:\Users\edu\Desktop\Python Automation\01_helloworld.py')
print(base_path)

# Returns true if the file path actually exists
path_exists = os.path.exists(r'C:\Users\edu\Desktop\Python Automation\not_exists.py')
print(path_exists)

# Returns true if it is a file
is_file = os.path.isfile(r'C:\Users\edu\Desktop\Python Automation\01_helloworld.py')
print(is_file)

# Returns true if it is a folder
is_folder = os.path.isdir(r'C:\Users\edu\Desktop\Python Automation')
print(is_folder)

# Returns the size of a file in bytes
file_size = os.path.getsize(r'C:\Users\edu\Desktop\Python Automation\01_helloworld.py')
print(file_size)

# Returns a list of the file names inside a folder
file_names = os.listdir(r'C:\Users\edu\Desktop\Python Automation')
print(file_names)

# Finding the total size of all files in a folder
total_size = 0
for f in file_names:
    if os.path.isfile(f):
        total_size += os.path.getsize(f)
print(total_size)

# Creates new folders in a path given
# os.makedirs(r'C:\Users\edu\Desktop\folder_created')

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

# Copying and Moving files and folders (shutil)
# -------------------------------------------------------
import shutil

# Copy and move to another folder, you can rename the file too
shutil.copy(r'C:\Users\edu\Desktop\hello.txt', r'C:\Users\edu\Desktop\IC')

# Copy an entire folder
shutil.copytree(r'C:\Users\edu\Desktop\IC', r'C:\Users\edu\Desktop\backup')

# Move a file to a new location or rename a file
shutil.move(r'C:\Users\edu\Desktop\hello.txt', r'C:\Users\edu\Desktop\hello3.txt')


