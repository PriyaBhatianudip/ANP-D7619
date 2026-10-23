class Student:
    def __init__(self, x):
        self.x=x

    def __str__(self):
        return "Student Special Id "+str(self.x)

s1= Student(929)
print(s1)