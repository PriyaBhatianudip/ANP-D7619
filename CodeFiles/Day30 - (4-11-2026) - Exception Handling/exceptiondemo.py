class Calculator:
    def add(self, a,b):
        print("Sum : ", a+b)

    def sub(self, a,b):
        print("Sub : ", a-b)

    def multiply(self, a,b):
        print("Multiply : ", a*b)

    def divide(self, a,b):
        try:
            print("Divide : ", a/b)
            print("Division is closed!!")
        except ZeroDivisionError as ze:
            print("Can't divide a number by Zero!!")
            print("Error : ", ze)
            print("Args : ", ze.args)

    def modulus(self, a,b):
        try:
            print("Modulus : ", a%b)
        except ZeroDivisionError:
            print("Can't divide a number by Zero!!")

ob1 = Calculator()
ob1.add(45,47)
ob1.divide(45,9)
ob1.divide(56,0)
ob1.multiply(5,7)


