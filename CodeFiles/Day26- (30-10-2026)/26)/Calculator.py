class Calculator:
    def add(self, a, b):
        print("Calculator Class")
        print("Sum : ", a + b)


class Calc(Calculator):
    def add(self, a, b):
        print("Calc Class")
        if a <= 0 or b <= 0:
            print("Negative values can't be added!")
        else:
           super().add(a, b)


ob = Calc()
ob.add(33,132)
