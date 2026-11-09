# open a file using the 'with' statement

filename = input("Enter file name: ")

with open(filename, 'r') as fp:
    # data = fp.read()
    data = fp.readlines()
    print(data)

print("File is closed!!")