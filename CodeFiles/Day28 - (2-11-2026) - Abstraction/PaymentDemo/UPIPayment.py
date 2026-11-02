from payment import Payment

class UPIPayment(Payment):

    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process_payment(self):
        print("Processing UPI payment...")
        print("UPI ID:", self.upi_id)
        print("Amount:", self.amount)
        print("UPI payment successful!")

    def generate_receipt(self):
        print("UPI payment receipt generated.")