s1 = {11,33,'dfd',9.0}

# storing a list in set
list =[1,2,3,4,5,6,22,2]
s2 = set(list)
print(s2)

# store tuple as set
t1 = (88,322,33,45,202,292)
s3 = set(t1)
print(s3)

# to store a string as set
st= "welcome to python!!"
s4 = set(st)
print(s4)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))