# Q1. Find Differences Between Two Access Codes
# Two systems generate binary access codes:
# system1 = 12
# system2 = 10
# Write a Python program using the XOR (^) operator to find which bits are different between the two systems.
# Display:
# System 1: 12
# System 2: 10
# Different bits: ?
# Also print the binary representation of all three values.

system1 = 12
system2 = 10

# find the difference :
diff = system1 ^ system2

print("Difference between binary access codes : ", diff)

# bin():  it converts a number into its binary representation
print(f"System 1 access code : {bin(system1)}")
print(f"System 2 access code : {bin(system2)}")
print("Difference between binary access codes : ", bin(diff))


