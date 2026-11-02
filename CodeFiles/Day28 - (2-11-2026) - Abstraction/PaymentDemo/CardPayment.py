from payment import Payment

class CardPayment(Payment):

    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process_payment(self):
        print("Processing Card payment...")
        print("Card payment successful!")

    def generate_receipt(self):
        print("Card payment receipt generated.")