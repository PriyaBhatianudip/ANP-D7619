class Employee:
    empid =0
    empname = ''
    age = 0

    def setDetails(self):
        self.empid = int(input("Enter employee id :"))
        self.empname = input("Enter employee name: ")
        self.age = int(input("Enter age :" ))

    def showDetails(self):
        print("Employee Id : ", self.empid)
        print("Employee Name : ", self.empname)
        print("Age : ", self.age)

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.setDetails()
emp2.setDetails()
emp3.setDetails()

emp1.showDetails()
emp2.showDetails()
emp3.showDetails()


