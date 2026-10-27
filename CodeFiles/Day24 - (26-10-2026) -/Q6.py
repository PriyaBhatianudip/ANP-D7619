# 6. Create a Person class.
# Derive Student and Faculty from Person.
# Then create a ResearchAssistant class that inherits
# from both Student and Faculty.
# Display the details available from the parent classes.

class Person:
    def setDetails(self, personName, age):
        self.personName = personName
        self.age = age

class Student(Person):
    def setStudentRecord(self, rollno, course, marks):
        self.rollno =rollno
        self.course = course
        self.marks = marks

class Faculty(Person):
    def setFacultyRecord(self, empid,exp, salary):
        self.empid = empid
        self.exp = exp
        self.salary = salary

class ResearchAssistant(Student, Faculty):
    def showDetails(self):
        print("Roll No : ", self.rollno)
        print("Student Name : ", self.personName)
        print("Student Age : ", self.age)
        print("Student Course : ", self.course)
        print("Student Marks : ", self.marks)
        print("Faculty Id : ", self.empid)
        print("Faculty Salary : ", self.salary)

student = ResearchAssistant()
student.setDetails("Karan Singh", 23)
student.setStudentRecord(101, "Python", 89)
student.setFacultyRecord(1101, 8, 80000)
student.showDetails()