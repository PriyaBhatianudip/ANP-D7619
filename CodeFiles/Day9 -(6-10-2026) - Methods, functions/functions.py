# Banking Application

userid = "abc@gmail.com"
password = "abc#123"
balance = 70000

def menu():
    # menu of options
    print("-------------------------------------")
    while (True):
        print("1. View Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change Password")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        print("-------------------------------------")
        if choice == 1:
            print("Balance : ", balance)
        elif choice == 2:
            # withdraw
            print("Enter Amount : ")
            amt= int(input("Enter Amount: "))
            withdrawAmount(amt)
        elif choice == 3:
            # deposit
            depositAmount()
        elif choice == 4:
            # change password
            changePassword()
        elif choice == 5:
            print("Goodbye!!")
            break
        else:
            print("Invalid Choice")

def withdrawAmount(amount):
    global balance

    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"Rs. {amount} withdrawn successfully!!")
        print("Updated Balance: ", balance)

def depositAmount():
    global balance

    amt = int(input("Enter amount : "))
    if amt < 0:
        print("Invalid Amount")
    else:
        balance += amt
        print(f"Rs.{amt} deposited successfully!!")
        print("Updated Balance: ", balance)

def changePassword():
    global password
    #  user must get only three attempts to provide incorrect password
    # otherwise program should exit..

    attempts=0
    while attempts < 3:
        oldpwd = input("Enter Old Password : ")
        if oldpwd != password:
            print("Password does not match ")
            attempts += 1
        else:
            newpwd = input("Enter new Password : ")
            retype = input("Retype New Password : ")

            if retype != newpwd:
                print("Password does not match")
            else:
                password = newpwd
                print(f"Password changed successfully!!")
            break
    if attempts == 3:
        print("Maximum number of attempts reached!!")

# Assignment
#  create a banking application using functions, where user must
#  be able to perform folowing tasks:-
# 1. Check balannce
# 2. withdraw amount
# 3. deposit amount
# 4. change password
# 5. exit when user chooses option number 5
# Tasks:
# Q1.  create another function to check login credentials
# if credentials match with the given credentials, only then
# allow user to enter the menu
# Q2. in change password, check password strength
# create another function to check password strength
# call menu function
menu()