# # to create a list
# list1 =[88,299,992,98, 'jj', 898.02]
#
# # list using constructor
# list2 = list([99,33,29,22])
#
# print(list1)
# print(list2)
#
# # list using user input
# names =[]  # it will create an empty list
# age=[]
# # n = int(input("Enter number of elements to store : "))  #5
# #
# # for i in range(n):  #   i =0 1   i<n
# #     x= input("Enter name : ")  # aa
# #     names.append(x)  #[ 'aa', 'bb']
# #
# #     age.append(int(input("Enter age : ")))  #  age[22, 33]
# #     # names.append(input("Enter name : "))
# #
# # print("Employee Names : ", names)
# # print("Age : ", age)
#
# # add elements of list2 into list1
# list1.extend(list2)
#
# print("List 1 after extending elements from list2 : ", list1)
#
# value = int(input("Enter a value : "))
# index = int(input("Enter the index : "))
#
# print(f"List2 before insertion : {list2}")
# list2.insert(index, value)
#
# print(f"List2 after adding new element at {index} : {list2}")
# print(list2[4])
#
# list2.insert(-2, 1000)
# print(list2)

# --------------------------------------
list2 = list([99,33,29,22])
list2.remove(29)
print(f"List 2 after removing 89 : {list2}")

ob1 =[[12,22],[334,48,3],[33,44,90]]
#       0         1           2
print("Length : ", len(ob1))
print(ob1)
ll = [334,48,3]
ob1.remove(ll)
print(ob1)
# ob1.remove(33)
# print(ob1)
ob1.pop(1)
print(ob1)
ob1.clear()
print(ob1)
print("Length : ", len(ob1))
