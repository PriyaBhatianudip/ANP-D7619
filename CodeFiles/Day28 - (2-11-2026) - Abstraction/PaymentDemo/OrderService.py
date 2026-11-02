class OrderService:

    def place_order(self, payment):

        print("\nProcessing your food order...")

        payment.process_payment()

        payment.generate_receipt()

        print("\nOrder placed successfully!")