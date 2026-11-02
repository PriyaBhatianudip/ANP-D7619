# if parent class constructor is initialized , but child class has no constructor, then parent class constructor will be called and will be initialized.
#

class A:
    def __init__(self, name):
        self.name = name
        print("Class A Constructor")

class B(A):
    pass

# b = B() if we don't provide any parameter, it will throw a TypeError
# as only parent class has a constructor, then  b class object will be created
# according to the parent class init method
b = B("Python")
print(b.name)


# Case 2:  ->  Both of the classes has their own init method with parameters:-
# if we create the object of child class, then by default its init method will be called and its variables will be initialized. but parent class constructor will not be called.
class X:
    def __init__(self, name=""):
        print("Class X ")
        self.name = name

class Y(X):
    def __init__(self, course):
        print("Class Y ")
        self.course = course

class Z(X):
    def __init__(self, course, name=""):
        super().__init__(name)
        print("Class Z ")
        self.course = course

y = Y("Python")
print(y.course)
# print(y.name)

z = Z("Python", "Harsh")
print(z.name)
print(z.course)

# # Case 3: if Both of the classes has init() method, then child
# # class constructor will be executed. parent init method will
# # not be called, unless we provide a command to call it from
# # the child class constructor or method.'
#
# class M:
#     def __init__(self):
#         print("Class M ")
# class N(M):
#     def __init__(self):
#         print("Class N ")
# n = N()
