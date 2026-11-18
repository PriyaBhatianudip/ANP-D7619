import json
from operator import index

employeedata = {"id":101, "name":"Aryan", "age":20,
                "salary":55000}

jsondata = json.dumps(employeedata)

print(jsondata)
print("Type : ", type(jsondata))

print("-----------------------------------------")
jsondata = json.dumps(employeedata, indent=5,
                      sort_keys=True)

print(jsondata)
print("Type : ", type(jsondata))
print("-------------------------------------------------")
# to create a json type data
datajson = '''
{
    "id":101,
    "name":"Aryan",
    "age":20
}
'''
emp = json.loads(datajson)
print("Employee id : ", emp['id'])
print("Employee name : ", emp['name'])
print("Employee age : ", emp['age'])

print("Type of json var : ", type(datajson))
print("type of emp object : ", type(emp))

print("-----------------------------------------------")
# json array
jsondata = '["abc", "xyz", "ddd","eee"]'

# python list
values = json.loads(jsondata)
print("Values : ", values)

print("-----------------------------------------------")

employeedata = {"id":101, "name":"Aryan", "age":20,
                "salary":55000}
file = open("employee.json", "w")
json.dump(employeedata, file, indent=4)
file.close()
print("Data saved successfully!!")
print("-----------------------------------------------")

with open("employee.json", "r") as file:
    data = json.load(file)

print(data)
print("Type of object : ",type(data))