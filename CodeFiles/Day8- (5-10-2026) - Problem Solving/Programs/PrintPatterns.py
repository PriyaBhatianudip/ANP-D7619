rows = int(input("Enter number of rows : "))
print("Pattern 2")
for r in range(rows, 0, -1):
    for c in range(r, 0, -1):
        print(c, end=" ")
    print()

# 3.
# ----1         1 time      r=5  col= 6  col>r(5)
# ---1 2        2 times     r=4  col = 6, 5    col>r(4)
# --1 2 3       3 times     r=3  col = 6,5 4    col>r(3)
# -1 2 3 4      4 times     r=2
# 1 2 3 4 5     5 times     r=1

print("Pattern 3")
for r in range(rows, 0, -1):  # r = 5 r>0
    # print(f"r={r}")
    for c in range(r, 1, -1):  # c=r=5  c>0
        # print(f"c={c}")
        print(" ", end=" ")
    for col in range(rows+1, r, -1): # col=6   col>r(5)
        # print(f"col={col}")
        print(col, end=" ")
    print()
