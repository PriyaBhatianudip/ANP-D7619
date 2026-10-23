class student:
    collegename="ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"College Name : {self.collegename}")
        print(f"Student Name : {self.name}")
        print(f"Marks : {self.marks}")

s1 = student("Aman Kumar", 76)
s2 = student("Namit", 89)

student.collegename ="nnnmn"
# if we access a class variable using the object,
# then python creates an instance variable with that name
# instead of accessing the class variable.

s1.display()
print("-----------------------")
s2.display()

print("s1 : ", s1.__dict__)  # properties of s1
print("s2 : ", s2.__dict__)  # properties of s2
print("student : ", student.__dict__) # properties of student class

# print("name : ", student.name)
# print("marks : ", student.marks)