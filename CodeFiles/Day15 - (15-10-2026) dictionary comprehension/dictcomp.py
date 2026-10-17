squares = {i:i*i for i in range(1,6)}
print(squares)

# convert two lists into a dictionary
names=["aa","bb","cc","dd"]
marks=[88,77,98,67]
# result = {"aa":88, "bb":77, "cc":98, "dd":67}

result={}
for i in range(len(names)):
    result[names[i]]=marks[i]

print(result)

result = {names[i]:marks[i] for i in range(len(names))}
print(result)

# store all even numbers in a dictionary along with
# their serial number as key
#  How many even numbers you want to print : 6
# output = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6:12}
# using if condition and dictionary comprehension.
# Store only odd numbers from 1 to n,
# with their squares as values.
# - Input: 7
# - Output: {1: 1, 3: 9, 5: 25, 7: 49}
n = int(input("How many even numbers you want to store : "))
result = {i: i*2 for i in range(1, n+1) if (i*2) % 2 == 0}
# i=1  , 1 to 6
# 1*2=2%2==0 true   {1:2}
# i=2
# 2*2=4%2==0  true  {1:2, 2:4}

