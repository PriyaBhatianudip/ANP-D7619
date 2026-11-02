from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass