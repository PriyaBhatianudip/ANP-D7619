# 1. Create a Person class with name and age attributes.
# Create a Student class that inherits from Person and adds
# roll_no. Display all details using a Student object.

class Person:
    def setDetails(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))


class Student(Person):
    def show(self):
        self.setDetails()
        self.roll_no = input("Enter roll number: ")

    def displayDetails(self):
        print("===========================")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


s1 = Student()
s1.show()
s1.displayDetails()
