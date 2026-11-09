# 1. obtain data from user
empdata = {}
# {"id" : 101, "name":"jj", "age" : 23}

empdata['id'] = int(input("Enter employee id : "))
empdata['name'] = input("Enter employee name : ")
empdata['age'] = int(input("Enter employee age : "))
empdata['salary'] = float(input("Enter employee salary : "))

# 2. open a file in write mode
file = open("employeedata.csv", "w")

# 3. write data into the file
file.write(f"Employee Id\tEmployee Name\tAge\tSalary\n")
file.write(f"{empdata['id']}\t{empdata['name']}\t{empdata['age']}\t{empdata['salary']}"
           f"\n")

# 4. close the file
file.close()