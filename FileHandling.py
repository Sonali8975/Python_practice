# /////////////Reading From File:


File1 = open("quotes.txt", "r")
print(File1.readlines())
print(File1.readline(4))


file_content = File1.read()
print(file_content)
print(type(file_content))

File1.close()
print(File1.closed)                 #Output is true or false

print(File1.name)
print(File1.mode)


# //Or
with open("quotes.txt", "r") as File1:
    line1 = File1.readline()
    line2 = File1.readline()
    line3 = File1.readline()
print(line1, line2, line3)


with open("quotes.txt", "r") as File1:
    for line in File1:
        print(line, end="")


with open("quotes.txt", "r") as File1:
    print(File1.readline(2))
    print(File1.readline(6))
    print(File1.readline(2))
# print(line1, line2)

with open("quotes.txt", "r") as File1:
    line1 = File1.read()
    print(line1)


with open("quotes.txt", "r") as File1:
    i = 0
    for line in File1:
        print("This is Iteration", i, ": ", line, end="")
        i += 1


with open("quotes.txt", "r") as File1:
    line1 = File1.readlines()
print(line1[1])


# /////////////Writing To File:

with open("exp.txt", 'w') as File1:
    File1.write("Sonali Sindhu Sahebrao Sangle")
    # print(File1.readlines())


with open("exp.txt", 'w') as File1:
    File1.write("Sonali Sindhu Sahebrao Sangle\n")
    File1.write("Analyst/ Software Engineer\n")
    # print(File1.readlines())


lines = ["This is line 1\n", "This is line 2\n", "This is line 3\n", "This is line 4\n"]
with open("exp.txt", 'w') as File1:
    for line in lines:
        File1.write(line)


with open("exp.txt", "r") as readFile:
    with open("exp1.txt", "w") as writeFile:
        for line in readFile:
            writeFile.write(line)

with open("exp.txt", "a") as File2:
    File2.write("**** THIS IS NEW LINE 5 ****")

with open("exp.txt", "a+") as File2:
    File2.write("\n**** THIS IS NEW LINE 6 ****")
    print(File2.readlines())

with open("exp.txt", "r+") as File2:                    #It will not truncate the file
    File2.write("\n**** THIS IS NEW LINE 7 ****")
    print(File2.readlines())

with open("exp.txt", "w+") as File2:                    #It will truncate the file
    File2.write("\n**** THIS IS NEW LINE 8 ****")
    print(File2.readlines())


with open('exp1.txt', 'a+') as testwritefile:
    # print(testwritefile.tell())
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):  # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bytes from beginning.
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))
