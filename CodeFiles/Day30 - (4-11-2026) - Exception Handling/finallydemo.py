# input a file name with file path and try to open this file
# and get its content.
filename = input("Enter file name: ")
try:
    file = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist")
else:
    print("File opened successfully!!")
    # to read the content of the file :-
    print(file.read())
finally:
    if file is not None:
        file.close()
        print("File closed successfully!!")

#to check if an object is empty or not, we can check it for None value
