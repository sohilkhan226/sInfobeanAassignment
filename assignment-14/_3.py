# 3. Perfect Number Reward System

# A gaming company rewards users if entered number is a Perfect Number.

# (Perfect Number = sum of proper factors equals number)

# Write a program using for-else loop to:

# - Find sum of proper factors
# - If sum equals number print Reward Unlocked
# - Else print Try Again

# Input:
# 6

# Output:
# Reward Unlocked


n = int(input())

total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
else:  # Executes after loop completes normally
    if total == n:
        print("Reward Unlocked")
    else:
        print("Try Again")



#

# n = int(input())

# total = 0
# i = 1

# while i < n:
#     if n % i == 0:
#         total += i
#     i += 1

# if total == n:
#     print("Reward Unlocked")
# else:
#     print("Try Again")