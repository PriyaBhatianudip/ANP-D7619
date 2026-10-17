# check whether a number is armstrong or not

# determine the number of digits
def countdigits(n):
    count = 0
    while n > 0:
        count += 1
        n -= 1
    return count

x= int(input("Enter a number: "))
digits = countdigits(x)
print("Number of digits : ", digits)