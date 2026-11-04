# input a file name with file path and try to open this file
# and get its content.
filename = input("Enter file name: ")

try:
    file = open(filename)
except FileNotFoundError:
    print("File does not exist")
else:
    print("File opened successfully!!")
    # to read the content of the file :-
    print(file.read())
    file.close()