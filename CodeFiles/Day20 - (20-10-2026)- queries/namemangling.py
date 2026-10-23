class Student:
	def __init__(self):
		self.__marks = 90

	def display(self):
		print(self.__marks)

s1= Student()
s1.display()
print(s1._Student__marks)

