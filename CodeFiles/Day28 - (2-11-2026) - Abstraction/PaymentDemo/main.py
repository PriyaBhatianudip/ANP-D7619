from UPIPayment import UPIPayment
from CardPayment import CardPayment
from CashPayment import CashPayment
from OrderService import OrderService

print("===== FOOD DELIVERY APPLICATION =====")

amount = float(input("Enter food order amount: "))

print("\nSelect Payment Method")
print("1. UPI")
print("2. Credit Card")
print("3. Cash on Delivery")

choice = int(input("Enter your choice: "))

if choice == 1:
    upi_id = input("Enter UPI ID: ")
    payment = UPIPayment(amount, upi_id)

elif choice == 2:
    card_number = input("Enter card number: ")
    payment = CardPayment(amount, card_number)

elif choice == 3:
    payment = CashPayment(amount)

else:
    print("Invalid payment option")
    exit()

service = OrderService()

service.place_order(payment)