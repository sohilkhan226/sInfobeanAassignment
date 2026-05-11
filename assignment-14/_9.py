# 9.
#  Bike Service Kilometer Checker

# A bike needs service every 3000 km.

# Write a program to:

# - Read travelled kilometers
# - Print every service checkpoint till entered km

# Input:
# 10000

# Output:
# 3000 6000 9000

km = int(input())
i = 3000

while i <= km:
    print(i, end=" ")
    i += 3000
print()


#

# km = int(input())

# for i in range(3000, km + 1, 3000):
#     print(i, end=" ")
# print()