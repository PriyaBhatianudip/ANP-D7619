# open a file using the 'with' statement

filename = input("Enter file name: ")

with open(filename, 'r') as fp:
    data = fp.read(5)
    print(data)

    print("Current cursor position : ", fp.tell())
    data = fp.read(5)
    print(data)
    print("Current cursor position : ", fp.tell())

    fp.seek(20)
    print(fp.read(10))
    print("Current cursor position : ", fp.tell())
print("File is closed!!")