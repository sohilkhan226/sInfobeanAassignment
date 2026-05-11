# Note: Read all the values from user. Use loops wherever required.

# ---

# 1. Sum of First N Natural Numbers
# A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
# Write a program to calculate the **total points earned after n days** by summing all natural numbers up to n using loops.

# Input: n = 10
# Output: Total Points = 55

# ---

n = int(input("Enter n: "))

total = 0
i = 1

while i <= n:
    total = total + i
    i = i + 1

print("Total Points =", total)


# 

# # User se input lena
# n = int(input("Enter n: "))

# total = 0

# # for loop ka istemal (1 se lekar n tak chalega)
# # range(1, n + 1) isliye likha hai kyunki range last number ko include nahi karta
# for i in range(1, n + 1):
#     total = total + i

# print("Total Points =", total)






















