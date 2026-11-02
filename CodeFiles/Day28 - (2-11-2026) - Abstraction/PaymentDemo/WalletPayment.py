from payment import Payment

class WalletPayment(Payment):

    def process_payment(self):
        print("Processing Wallet Payment")

    def generate_receipt(self):
        print("Wallet Receipt Generated")