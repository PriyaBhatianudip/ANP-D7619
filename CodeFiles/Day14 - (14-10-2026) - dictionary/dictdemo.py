data = {1:"aa", 2:"bb", 3:"cc",4:"dd", 5:"ee", 6:"ff", 7:"gg", 8:"hh", 9:"ii"}
print(data)

# to print each pair separately:-
# -> keys()  : it returns the list of keys.
#  -> to get the value :  ob[key]
print("Dictionary Elements:- ")
for key in data.keys():  #  key=1  [1,2,3,4,5,6,7,8,9]
    print(f"{key} is the key of  {data[key]}")

# ->  items():  it will return both key and value pair
print("Elements : ", data.items())

# items() function in for loop
for key,value in data.items():  #
    print(f"{key} is {value}")


#  get(key, defaultvalue)
no = int(input("Enter your rollno : "))
print(f"{no} - {data.get(no,"Invalid Roll Number!!")} ")

print(f"{no} - {data.get(no,00)} ")

# values() : returns all the value parts from dictionary
print("Values  : ", data.values())

for x in data.values():
    print(x)

# -> pop():  removes the key-value pair whose value we will specify.
# print("key-value : ", data.pop(no))
print("Dictionary after pop function : ", data)

# only remove the first key-value pair
print("pop item : ", data.popitem())
print("Dictionary after pop function : ", data)

# add a new key value pair
# -> update()
data.update({10:"eed"})

print("dictionary after update function : ", data)

# to add value to the dictionary
# data[new key] = value

data[11] ="jk"
print("dictionary after update function : ", data)

# to create a dictionary with default value and keys
keys = [77,78,79,80]
newdata = dict.fromkeys(keys, "--")
print(newdata)

newdata[77] = "add"
print(newdata)

newdata.clear()
print(newdata)

# to change an existing value
data[no] = input("Enter new name : ")

print(data)