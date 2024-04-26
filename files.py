import os

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""

#Read a file

file = open("demofile.txt","rt")
# print(file.read())
# print(file.read(5))
# print(file.readline())
# print(file.readline())

for x in file:
    print(x)

# Close a file
file.close()

# Append content in an existing file
file = open("demofile2.txt","a")
file.write("Now the file has more content!")
file.close()

file = open("demofile2.txt", "r")
print(file.read())

# Overwrite the content

file = open("demofile2.txt", "w")
file.write("Woops! I have deleted the content!")
file.close()

file = open("demofile2.txt","r")
print(file.read())

# Create a new file
file = open("newfile.txt", "x")
file.close()

# Create a file if it does not exist
file = open("myfile.txt", "w")
file.close()

# Remove file
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")

# Delete folder
os.rmdir("myfolder") # It will be removed only if it is empty