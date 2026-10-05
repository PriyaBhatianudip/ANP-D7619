# Q4. wap to print all prime numbers within the given range.
# Input start number :  50
# Input end number :  150

start = int(input("Enter First Number : "))  #  1
end = int(input("Enter last Number : "))  # 10


for n in range(start, end+1):  #  n= 1 2  n<11
    for i in range(2, n//2 + 1):  #  i= 2 i< 2//2+1(2)
        if n % i == 0:
            break
    else:
        print(n)

