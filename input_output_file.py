# file path
# C:\pythonProjectLerning\files

with open('C:/pythonProjectLerning/files/example.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # # Print the content

    # Open the file in write mode
with open('C:/pythonProjectLerning/files/example.txt', 'w') as file:
    # Write test to the file
    file.write('Hello, world!\n')
    file.write('This is a simple text.\n')
    file.write('I love Ariel and Aviv')
    print(content)

    # Create and read new file
with open('C:/pythonProjectLerning/files/example2', mode='w') as f:
    f.write('I created this file')

with open('C:/pythonProjectLerning/files/example2', mode='r') as f:
    print(f.read())

# Open the file in read mode
with open('C:/pythonProjectLerning/files/example3.txt', mode= "r") as file:
    # Read and print each line of the file
    for line in file:
        print(line.strip())  # Strip removes the newline character at the end of each line


