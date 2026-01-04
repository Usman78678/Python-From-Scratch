# the os module provides a way of using operating system dependent functionality like reading or writing to the file system.

import os

# Specify the directory path
path = "/Games"

# Get the list of files and folders
items = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in items:
    print(item)
