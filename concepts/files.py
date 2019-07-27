# Python has functions for creating, reading, updating, and deleting files.

# Open file, create file
# if you run this line below, new file will be created
# w flag is to overide / replace and write
myFile = open('myfile.txt', 'w')

# Get info // display file name
print('Name: ', myFile.name)
print('is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# open file, write to it and close it
myFile.write('I love Python')
myFile.write(' and JS')
myFile.close()

# append to file // open file as append bcoz we dont want to replace file contents
# we are appending more text to it

# open file to append # a flag is to append
myFile = open('myfile.txt', 'a')
myFile.write(' and ReactJS')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
# 50 is characters length
fileContents = myFile.read(50)
print(fileContents)
