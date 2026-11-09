from exceptionclass import AgeError

class VoterList:
    def validateVoter(self):
        age = int(input("Enter Age : "))
        try:
            if age < 18:
                raise AgeError("Age must be greater than "
                               "or equals to 18", age)
        except AgeError as ve:
            print(ve)
        else:
            print("You are eligible for voting")

ob = VoterList()
ob.validateVoter()