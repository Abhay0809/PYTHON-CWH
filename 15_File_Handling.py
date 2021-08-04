# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
f = open('File_IO/sample.txt')  # by default the mode is r
# data = f.read()
data = f.read(5)  # reads first 5 characters from the file
print(data)
f.close()

f = open('File_IO/sample.txt')
# read first line
data = f.readline()
print(data)

# Read second line
data = f.readline()
print(data)

# Read third line
data = f.readline()
print(data)

# Read fourth line... and so on...
data = f.readline()
print(data)
f.close()

# Writing in a File
f = open('File_IO/another.txt', 'w')
f.write("I am writing")
f.close()

with open('File_IO/another.txt', 'r') as f:
    a = f.read()
with open('File_IO/another.txt', 'w') as f:
    a = f.write("me")
print(a)







