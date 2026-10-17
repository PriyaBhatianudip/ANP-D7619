def reverseNumber(num):
    # to covert number into string, use str() function
    n = str(num)  #123
    reverse = n[::-1]  #  321
    print("Original number: ", n)
    print("Reversed number: ", reverse)
    if n == reverse:
        print("palindrome number")
    else:
        print("Not a palindrome")

n = int(input("Enter a number: "))
reverseNumber(n)