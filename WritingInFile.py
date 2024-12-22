# w for writing
# r for reading
# r+ for reading and writing
# a for appending
file = open("./data.csv", "w")
file.write("id,name,email\n")
file.write("1,haroon,haroon@gmail.com\n")
file.write("2,sameer,sameer@gmail.com\n")
file.write("3,umar,umar@gmail.com\n")
file.close()

# r+ means the file needs to exists before writing
# anotherfile = open("./details.csv", "w")
anotherfile = open("./details.csv", "r+")
anotherfile.write("id,name,email\n")
anotherfile.write("1,haroon,haroon@gmail.com\n")
anotherfile.write("2,sameer,sameer@gmail.com\n")
anotherfile.write("3,umar,umar@gmail.com\n")
anotherfile.close()

onemorefile = open("./hello.csv", "a")
onemorefile.write("id,name,email\n")
onemorefile.write("1,haroon,haroon@gmail.com\n")
onemorefile.write("2,sameer,sameer@gmail.com\n")
onemorefile.write("3,umar,umar@gmail.com\n")
onemorefile.close()
