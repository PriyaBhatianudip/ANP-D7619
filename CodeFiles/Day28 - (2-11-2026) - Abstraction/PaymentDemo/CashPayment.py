from payment import Payment

class CashPayment(Payment):

    def process_payment(self):
        print("Order confirmed!")
        print("Payment will be collected on delivery.")

    def generate_receipt(self):
        print("COD receipt generated.")