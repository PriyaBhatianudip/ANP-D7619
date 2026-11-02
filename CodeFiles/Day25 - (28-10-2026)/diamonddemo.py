class A:
    def showDetails(self):
        print("Class A called...")


class B(A):
    def showDetails(self):
        print("Class B called...")


class C(A):
    def showDetails(self):
        print("Class C called...")

class D(C, B):
    pass

d = D()
d.showDetails()

print("MRO : \n", D.mro())
