# Copying and Moving files and folders (shutil)
# -------------------------------------------------------
import shutil

# Copy and move to another folder, you can rename the file too
shutil.copy(r'C:\Users\edu\Desktop\hello.txt', r'C:\Users\edu\Desktop\IC')

# Copy an entire folder
shutil.copytree(r'C:\Users\edu\Desktop\IC', r'C:\Users\edu\Desktop\backup')

# Move a file to a new location or rename a file
shutil.move(r'C:\Users\edu\Desktop\hello.txt', r'C:\Users\edu\Desktop\hello3.txt')

# Deleting files and folders
# -------------------------------------------------------
import os

# Deletes a single file
os.unlink(r'C:\Users\edu\Desktop\hello3.txt')

# Deletes an empty folder
os.rmdir(r'C:\Users\edu\Desktop\emptyFolder')

# Deletes a folder and all of its content
shutil.rmtree(r'C:\Users\edu\Desktop\deleted')

# Deleting all .txt files in a folder
for file_name in os.listdir(r'C:\Users\edu\Desktop\files'):
    if file_name.endswith('.txt'):
        os.unlink(os.path.join(r'C:\Users\edu\Desktop\files',file_name))

# Send the files to the trash and do not remove them permanently
import send2trash

send2trash.send2trash(r'C:\Users\edu\Desktop\importantFile.txt')

# Walking a directory tree
# -------------------------------------------------------
for folder_name,sub_folders, file_names in os.walk(r'C:\Users\edu\Desktop\dirTree'):
    print('The folder is' + folder_name)
    print('The subfolders are' + str(sub_folders))
    print('The filenames are' + str(file_names))