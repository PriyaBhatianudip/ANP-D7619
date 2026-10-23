class BankAccount:
    def __init__(self, balance, minbalance):
        self.__balance=balance
        self._minbalance = minbalance

    def displayBalance(self):
        print("Balance : ", self.__balance)

a1 = BankAccount(70000, 5000)

a1.displayBalance()
print("Minimum balance : ", a1._minbalance)
# print("Balance : ", a1.__balance)