# Case 1:  Both parent and child does not have any init method. In these cases default behaviour of
# classes from the object class is followed.

class A:
    def show(self):
        print("Class A ")

class B(A):
    def show(self):
        print("Class B ")

b = B()
b.show()

# Case 2:  If parent has an init method, but child class doesn't
# have any init method. Then python automatically calls the
# parent class init method.

class X:
    def __init__(self):
        print("Class X ")
class Y(X):
    pass

y = Y()

# Case 3: if Both of the classes has init() method, then child
# class constructor will be executed. parent init method will
# not be called, unless we provide a command to call it from
# the child class constructor or method.'

class M:
    def __init__(self):
        print("Class M ")
class N(M):
    def __init__(self):
        print("Class N ")
n = N()
