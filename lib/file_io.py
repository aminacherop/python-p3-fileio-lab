from pathlib import Path

def write_file(file_name, file_content):
    file_name = str(file_name)  
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, 'w') as file:
        file.write(file_content)
        
        
        #What it does:

# Takes in a file_name and some file_content.

# If file_name is a Path object, it converts it to a string.

# If it doesn't already end with .txt, it adds it.

# Uses Python’s open() function in write mode ('w') which:

# Creates a new file if it doesn't exist.

# Overwrites the file if it does exist.

# Writes the content into the file.






def append_file(file_name, file_content):
    file_name = str(file_name)
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, 'a') as file:
        file.write(file_content)
#         What it does:

# Same steps as write_file for handling the file name.

# Opens the file in append mode ('a'), which:

# Creates the file if it doesn’t exist.

# Appends content to the end of the file if it does exist.

# Adds file_content to the existing contents.

 
 
 



def read_file(file_name):
    file_name = str(file_name)
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, 'r') as file:
        return file.read()

# What it does:

# Converts the file name to a string and ensures it ends in .txt.

# Opens the file in read mode ('r').

# Reads and returns the file's content as a single string.

