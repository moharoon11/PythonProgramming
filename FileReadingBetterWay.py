import os.path

# filename = "./data.csv"
filename = "data.csv"

if(os.path.isfile(filename)) :
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist!")
