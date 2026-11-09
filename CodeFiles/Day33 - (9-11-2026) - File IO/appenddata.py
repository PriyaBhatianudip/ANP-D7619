import os

n = int(input("Enter number of employees : "))
file = open("employeedata.csv", "a")

if not os.path.exists("employeedata.csv"):
    file = open("employeedata.csv", "a")
    file.write(f"Employee Id\tEmployee Name\tAge\tSalary\n")

for i in range(n):
    # 2. obtain data from user
    empdata = {}
    empdata['id'] = int(input("Enter employee id : "))
    empdata['name'] = input("Enter employee name : ")
    empdata['age'] = int(input("Enter employee age : "))
    empdata['salary'] = float(input("Enter employee salary : "))

    # 3. write data into the file
    file.write(f"{empdata['id']}\t{empdata['name']}\t{empdata['age']}\t{empdata['salary']}"
               f"\n")

# 4. close the file
file.close()