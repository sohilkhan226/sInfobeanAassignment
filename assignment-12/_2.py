# 2. Count Numbers Divisible by 7 Between Two Numbers

# A company filters lucky coupon numbers divisible by 7.
# Write a program using loops to count such numbers in range.

# Input:
# 1 30

# Output:
# Count = 4

start, end = map(int, input().split())

count = 0
i = start
while i <= end:
    if i % 7 == 0:
        count += 1
    i += 1

print("Count =", count)

#
# start, end = map(int, input().split())

# count = 0
# for i in range(start, end + 1):
#     if i % 7 == 0:
#         count += 1

# print("Count =", count)