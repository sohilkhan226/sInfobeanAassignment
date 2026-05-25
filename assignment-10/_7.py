# **7. Count Even Digits**
# A data analyst is analyzing numeric IDs and needs to determine how many
# digits in the ID are even.
# Write a program to **count the number of even digits in a given number using loops**.

# Input: 123456
# Output: Even digits count = 3




number = int(input("Enter a number: "))

original    = number
even_count  = 0

while original > 0:
    digit = original % 10
    if digit % 2 == 0:
        even_count = even_count + 1
    original = original // 10

print("Even digits count =", even_count)


# num = int(input("Enter a number: "))

# even_count = 0
# temp = num
# for _ in str(num):
#     digit = temp % 10
#     if digit % 2 == 0:
#         even_count += 1
#     temp //= 10

# print("Even digits count =", even_count)