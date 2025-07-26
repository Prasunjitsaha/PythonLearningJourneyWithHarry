import os  # Import the os module to interact with the operating system

# Set the path of the directory you want to list
# '.' means the current working directory
directory_path = '.'


contents = os.listdir(directory_path)

# Print each item in the directory
print("Contents of the directory:-")
for item in contents:
    print(item)
#@