class Address:
    def __init__(self, houseno="", locality="",city=""):
        self.houseno=houseno
        self.locality=locality
        self.city=city

    def displayAddress(self):
        print("Address : ",self.houseno,self.locality,self.city)

class Person:
    def __init__(self, name="", age=0, address=None):
        self.name=name
        self.age=age
        self.address=address
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        self.address.displayAddress()
class Salary():
    def __init__(self, basicsalary=0):
        self.basicsalary=basicsalary

    def calculateSalary(self):
        self.da = 0.05 * self.basicsalary
        self.ta = 0.07 * self.basicsalary
        self.pf = 0.12 * self.basicsalary
        self.totalsalary = self.basicsalary + self.da + self.ta + self.pf
        self.netsalary = self.totalsalary - self.pf

    def displaySalary(self):
        print("********Salary Details*********")
        print(f"Basic Salary: {self.basicsalary}")
        print(f"DA Salary: {self.da}")
        print(f"TA Salary: {self.ta}")
        print(f"PF Salary: {self.pf}")
        print(f"Total Salary: {self.totalsalary}")
        print(f"NetSalary: {self.netsalary}")

class Employee:
    def __init__(self, person=None, salary=None):
        self.person=person
        self.salary=salary

    def displayEmployee(self):
        print("===============Employee Details===============")
        self.person.printDetails()
        self.salary.displaySalary()


person = Person()
person.name = input("Enter Employee Name: ")
person.age = int(input("Enter Employee Age: "))

address = Address()
address.houseno =input("Enter Employee House Number: ")
address.locality =input("Enter Employee Locality: ")
address.city =input("Enter Employee City: ")
person.address= address

salary = Salary()
salary.basicsalary =float(input("Enter Employee Basic Salary: "))
salary.calculateSalary()

e1 = Employee(person, salary)
e1.displayEmployee()