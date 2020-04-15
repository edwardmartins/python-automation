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

# Creates a new folder in a path given
os.makedirs(r'C:\Users\edu\Desktop\folder_created')