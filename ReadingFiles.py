# if we use r as a flag we cannot to write operation
# only read operations are allowed
file = open("./data.csv", "r")
print(file.read())

file1 = open("./details.csv", "r")
for line in file1 :
    print(f"printing line {line}")

file1 = open("./details.csv", "r")
print(file1.readlines())

file.close()
file1.close()
