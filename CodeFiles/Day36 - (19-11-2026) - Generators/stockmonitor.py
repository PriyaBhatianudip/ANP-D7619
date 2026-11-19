import random
import time

def stockPriceGenerator():
    price = 1000

    while True:
        price += random.randint(-20,20)
        yield price
        time.sleep(2)

stock = stockPriceGenerator()

for i in range(10):
    current_price = next(stock)
    print(f"Current Stock Price is {current_price}")

    if current_price >1050:
        print("Price Alert: Consider Selling")
    elif current_price < 950:
        print("Price Alert: Consider Buying")
    else:
        print("Price is Normal!!")
    print("--------------------------------")