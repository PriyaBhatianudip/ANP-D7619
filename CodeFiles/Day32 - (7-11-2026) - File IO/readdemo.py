# input the filename with path
filename = input("Enter file name with path : ")
file = None

try:
    # open this file in the read mode
    file = open(filename, 'r')
except FileNotFoundError:
    print("File does not exist!!")
except PermissionError:
    print("Permission denied!!")
except OSError:
    print("Oops!! File name is not proper!!")
else:
    # read the data and store into a variable/object
    data = file.read()
    # perform operation over the data
    print("File Data :\n", data)
finally:
    # close the file once the task is done
    if file is not None:
        file.close()
