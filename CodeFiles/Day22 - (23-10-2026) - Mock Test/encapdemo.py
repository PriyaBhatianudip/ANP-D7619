class Employee:
    def __init__(self, acno=0, name=None, password=None):
        self.__acno = acno
        self.__name = name
        self.__password = password

    def getAcno(self):
        return self.__acno

    def getName(self):
        return self.__name

    def getPassword(self):
        return self.__password

    def setAcno(self, acno):
        self.__acno = acno

    def setName(self, name):
        self.__name = name

    def setPassword(self, password): self.__password = password
    def __str__(self): return ("------------------------------\n"
            + "Account Number : " + str(self.__acno) + "\nName : "
            + self.__name + "\nPassword : " + self.__password)


e1 = Employee()
e1.setAcno(int(input("Enter Account Number : ")))
e1.setName(input("Enter Name : "))
e1.setPassword(input("Enter Password : "))

print(e1)
