# 8.
#  ATM Note Counter

# A bank ATM dispenses ₹100 notes.

# Write a program to:

# - Read withdrawal amount
# - Count how many ₹100 notes needed using loop

# Input:
# 700

# Output:
# Notes = 7

amount = int(input())
notes = 0

while amount >= 100:
    amount -= 100
    notes += 1

print("Notes =", notes)



#

# amount = int(input())
# notes = 0

# for _ in range(amount // 100):
#     notes += 1

# print("Notes =", notes)