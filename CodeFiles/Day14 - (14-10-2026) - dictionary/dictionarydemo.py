#create a dictionary

ob = {"studentid":1101, "studentname":"Mamta", "age":22, "marks":88}
print("Dictionary Items : \n", ob)

ob2 = ob
print("Dictionary Items : \n", ob2)

ob1 = dict(studentid=1102, studentname="Rameez", age=23,marks=87)
print("Dictionary Items : \n", ob1)

print("Reference of ob :",id(ob))
print("Reference of ob1 : ",id(ob1))
print("Reference of ob2 : ",id(ob2))


