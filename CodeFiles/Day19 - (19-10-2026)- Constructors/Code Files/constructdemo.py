class Student:
    
    def __init__(self, nm, age, course, marks):
        self.name=nm
        self.age=age
        self.course=course
        self.marks=marks
        jj=322
    # self.name =  class data member
    # name =parameter -> local variable of constructor
    def showDetails(self):
        print("Student Details:")
        print(self.name)
        print(self.age)
        print(self.course)
        print(self.marks)

# s1 = Student("kk", 33, "Java", 87)
# s2 = Student("mm", 23, "Python", 89)
#
# s1.showDetails()
# s2.showDetails()
