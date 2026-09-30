# Permission values
Read = 1
Write = 2
Delete = 4

# Employee permissions
permissions = int(input("Enter a permissions : "))  #  5
# Check permissions using bitwise AND
print("READ:", "Allowed" if permissions & Read else "Not Allowed")
print("WRITE:", "Allowed" if permissions & Write else "Not Allowed")
print("DELETE:", "Allowed" if permissions & Delete else "Not Allowed")
#  permissions = 5  -> 0101
# read   = 0001
# write  = 0010
# delete = 0100

# 101  ->  First digit = read, second digit = write, third digit =  delete
# permission & read
#   0101    5
#   0001 &  1
# ----------
#   0001   ->  true
# ------------

#  for write permission ->  permission & write
#   0101   5
#   0010 &  2
# ----------
#   0000   ->  false
# ------------

# for delete permission ->  permission & delete
#   0101
#   0100 &
# ----------
#   0100   ->  true
# ------------