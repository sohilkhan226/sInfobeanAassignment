# 10. Student ID Validity Checker (Count Odd Digits)
# A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

# Write a program to count the number of odd digits in a given student ID using loops.

# Input:
# 572943

# Output:
# Odd Digits Count = 3

num = int(input("Enter student ID: "))
count = 0

while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count += 1
    num = num // 10

print("Odd Digits Count =", count)

#

# num = int(input("Enter student ID: "))
# temp = num
# count = 0

# for _ in str(num):
#     digit = temp % 10
#     if digit % 2 != 0:
#         count += 1
#     temp = temp // 10

# print("Odd Digits Count =", count)