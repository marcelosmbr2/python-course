# Create file
file = open('example.txt', 'w')

# Write some content to the file
file.write('Hello, this is a new file created using Python.\n')

# Close the file to save changes
file.close()

# Read file
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# Update file
file = open('example.txt', 'a')
file.write('This line is added to the existing file.\n')
file.close()

# Delete file
import os
os.remove('example.txt')