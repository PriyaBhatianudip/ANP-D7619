class AgeError(Exception):
    def __init__(self, message, age):
        self.age = age
        self.message = f"Age {self.age} : {message}"

        super().__init__(self.message)