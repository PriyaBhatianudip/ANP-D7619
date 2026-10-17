s1 = "Hello Python!!"
#     01234567890123
# H e l l o  P y t h o n ! !
#                     -3 -2-1
print(s1)
# access only first character
print("First character : ", s1[0])
print("sixth index : ", s1[6])
print("last 3rd index : ", s1[-3])
print("reverse  string : ", s1[::-1])
print("string from 5th index : ", s1[5::])
print("string from -1 to -7 : ", s1[-3:-9:-1])
print("extract only python using decrement : ", s1[11:5:-1])
ss = s1.split()
print(ss)
print(ss[-1])
print(s1.split()[-1])
s2="id, name, age, salary"
print(s1.split())
columns = s2.split(',')
print(columns)

print("length of s1 : ,", len(s1))

firstname ="Varun"
lastname= "Sharma"

print("Welcome "+firstname+" "+lastname)

print("-"*50)

name="Alice"
age=30
formatted_str1="My name is %s, and I am %d years old."%(name,age)
formatted_str2="My name is {},and I am {} years old.".format(name,age)
formatted_str3=f"My name is {name} and I am {age} years old."

print(formatted_str1)
print(formatted_str2)
print(formatted_str3)


first = "Hello"
second = "HEllo"
third = "World"

print(first == second)  # false
print(first == third) # false
print(first > second) #  72   > 104
print(first < second) # 72 < 104

# to print the unicode number of a character
char = "उ"
print(f"Unicode of {char} is {ord(char)}")
n = 2318
print(f"the unicode character of {n} is {chr(n)}")

