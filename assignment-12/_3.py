# 3. Display Numbers Ending with 5

# A supermarket tracks token numbers ending in 5.
# Write a program using loops to display numbers ending with 5 between two numbers.

# Input:
# 10 40

# Output:
# 15 25 35

start, end = map(int, input().split())

i = start
while i <= end:
    if i % 10 == 5:
        print(i, end=" ")
    i += 1
print()


#
# start, end = map(int, input().split())

# for i in range(start, end + 1):
#     if i % 10 == 5:
#         print(i, end=" ")
# print()