# Question 1

'''with open('File_IO/poem.txt') as f:
    d = f.read()
    if 'twinkle' in d:
        print("Twinkle is Present in Poem!")
    else:
        print("Twinkle is not Present in Poem!")'''

# Question 2


# Question 3

for i in range(2, 21):
    with open(f"File_IO/tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i * j}")
            if j != 10:
                f.write('\n')

# Question 4

with open("File_IO/sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("File_IO/sample.txt", "w") as f:
    f.write(content)

# Question 5

words = ["donkey", "kaddu", "mote"]

with open("File_IO/sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("File_IO/sample.txt", "w") as f:
        f.write(content)

# Question 6

with open("File_IO/log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")

# Question 7

content = True
i = 1
with open("File_IO/log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i += 1

# Question 8

with open("File_IO/this.txt") as f:
    content = f.read()

with open("File_IO/copy.txt", 'w') as f:
    f.write(content)

# Question 9

file1 = "File_IO/log.txt"
file2 = "File_IO/this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2= f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")

# Question 10

filename = 'File_IO/sample.txt'
with open(filename, "w") as f:
    f.write()

# Question 11

import os

oldname = "File_IO/sample2.txt"
newname = "File_IO/renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)




