class Employee:
    def __init__(self, empname="Unknown", salary=0):
        self.empname=empname
        self.salary=salary

    def showDetails(self):
        print(self.empname)
        print(self.salary)

e1 = Employee("aa", 77000)
e2 = Employee()

e1.showDetails()
e2.showDetails()
