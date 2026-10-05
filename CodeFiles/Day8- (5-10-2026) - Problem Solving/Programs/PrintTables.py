start = int(input("Enter First Number : "))
end = int(input("Enter lastNumber : "))

for i in range(start, end+1):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()


print("-----------------------Column Wise-------------------------------------")

for j in range(1, 11):    #   j = 1 2  j<11
    for i in range(start, end + 1):  #  i = 2,  i<11
        print(i * j, end="\t")  # 2     3   4   5
    print()
