# Create an Employee class with employee_id and name.
# Create a Salary class that inherits from Employee and
# adds basic_salary and bonus.
# Display the employee details and calculate the total salary.

class Employee:
    def empRegister(self):
        self.empId = input("Enter The Your Employee ID : ")
        self.empName = input("Enter Your Employee Name : ")


class Salary(Employee):
    def income(self):
        self.empRegister()
        self.basic_Salary = int(input("Enter Your salary : "))
        self.bonus = int(input("Enter Your bonus : "))
        self.Total = (self.basic_Salary + self.bonus)

    def showDetails(self):
        print("Employee ID is : ", self.empId)
        print("Employee Name : ", self.empName)
        print("Basic Salary : ", self.basic_Salary)
        print("Bonus : ", self.bonus)
        print("Total Salary is : ", self.Total)


obj2 = Salary()
obj2.income()
obj2.showDetails()