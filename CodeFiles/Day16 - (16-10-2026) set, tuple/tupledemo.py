# # unpacking means extracting each value from
# # the tuple dataset into individual variables.
#
t1= (22,44,77,90,59,99,45,77,2,24)
# a,b,*c =t1
# # a=22
# # b=44
# # c =[77,90,59,99]
# print(a)
# print(b)
# print(c)
# # extract first and last only
# a, *b, c=t1
# print(a)
# print(b)
# print(c)
# print("--------------------------------")
# *a, b,c =t1
# print(a)
# print(b)
# print(c)

a, b,*_ =t1
print(a)
print(b)

print("get value from 2nd index : ", t1[2])

print("All elements using loop")
for i in t1:
    if i % 2 == 0:
        print(i)

print("Elements of tuple : ", t1)
t2 = sorted(t1)
print("Tuple in Ascending order : ", t2)
t3 = sorted(t1, reverse=True)
print("Tuple in Descending order : ", t3)
first = t1.index(77)
print("index of 77(first occurrence) :",first)
# second = t1.index(77, first+1)
second = t1.index(77, t1.index(77)+1)
print("index of 77(second occurrence) :",second)

