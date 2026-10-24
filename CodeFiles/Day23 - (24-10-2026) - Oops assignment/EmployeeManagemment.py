class Employee:
    def __init__(self):
        print("Object is initialized...")
        self.__id = 0
        self.__name = ""
        self.__salary = 0.0

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def registerEmployee(self):
        self.setId(int(input("Enter Employee Id : ")))
        self.setName(input("Enter Employee Name : "))
        self.setSalary(float(input("Enter Employee Salary : ")))

        return self

    def displayEmployee(self):
        print("Employee Details")
        print(f"Employee id : {self.getId()}")
        print(f"Employee Name : {self.getName()}")
        print(f"Employee Salary : {self.getSalary()}")

e1 = Employee()
e1.registerEmployee()
e1.displayEmployee()

e2 = Employee()
e2.registerEmployee()
e2.displayEmployee()


