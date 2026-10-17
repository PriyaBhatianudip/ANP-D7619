fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []
for x in fruits:  #  x= mango
    if "a" in x:  #if "a" in mango
        newlist.append(x)  #apple , banana, mango
print(newlist)

ob = [x for x in fruits if "a" in x]
print(ob)

for x in fruits:
    print(x)

print([x for x in fruits])
print("---------------------------------")
[print(x) for x in fruits]

# convert in upper case
ch = "A"
print(ch)
# to get its ascii value
print(ord(ch))  #  65
# add 32 to the ascii value of ch
x = ord(ch)+32  # 97
print(x)
# convert it back into char form
# chr() for converting ascii into character
ch = chr(ord(ch)+32)  #97 -> a
print(ch)
items = ["Laptop", "", "TV", "Mouse", "", "", "keyboard", "", "Tab"]
items = [i for i in items if i != ""]
print(items)

print("------------------------------")
my_list = ["hello", "", "python", "", "world", ""]
new_List = [x for x in my_list if x!= ""]
print(new_List)

# true statement if condition else false statement
a=22
b=55
print(a) if a>b else print(b)


names = ["Laptop", "Mouse", "tv", "keyBoard", "taB"]
temp = []
for name in names:  #  name = Laptop
    nm = ""
    for ch in name:   #  ch = a
        if 'a' <=ch <='z':
            # ch = chr(ord(ch)-32)
            # nm += ch
            nm += "".join(chr(ord(ch)-32))
        else:
            nm += ch
    print(nm)
    temp.append(nm)
names= temp
print(names)

result = ["".join(chr(ord(ch)-32) if 'a' <=ch <='z' else ch for ch in name)
          for name in names]


items = ["Laptop", "TV", "Mouse", "keyboard","Tab"]
for index, name in enumerate(items):
    print(f"{index} : {name}")
# 0 : Laptop
# 1 : TV

[print(index, name) for index,name in enumerate(items)]

# print(r)

