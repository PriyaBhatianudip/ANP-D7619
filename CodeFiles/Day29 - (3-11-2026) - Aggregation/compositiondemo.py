class Room:
    def __init__(self, room_name, area):
        self.room_name=room_name
        self.area=area

    def display(self):
        print("Room : ", self.room_name)
        print("Area : ", self.area)

# class House:
# 	def __init__(self, housename, room_name, area):
# 		self.housename=housename
# 		self.room = Room(room_name, area)
#
# 	def display(self):
# 		print("House : ", self.housename)
# 		self.room.display()

class House:
    def __init__(self, housename):
        self.housename = housename

        self.rooms = [Room("Kitchen", 289),
                      Room("Bedroom", 459),
                      Room("Drawing Room", 400),
                      Room("Dining Room", 600)]

    def display(self):
        print("House : ", self.housename)
        for room in self.rooms:
            room.display()

h1 = House("My House")
h1.display()
