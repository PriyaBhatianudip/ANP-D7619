class Car:
    def registerCar(self):
        self.carname = input("Enter car name: ")
        self.price = float(input("Enter car price: "))
        self.company = input("Enter company name: ")

    def displayCarDetails(self):
        print(f"Car Name : {self.carname}")
        print(f"Company Name : {self.company}")
        print(f"Price  : {self.price}")

class MarutiDesire(Car):
    def carStart(self):
        print("Push the start button to start the car")
        
c1 = MarutiDesire()
c1.registerCar()
c1.displayCarDetails()
c1.carStart()
