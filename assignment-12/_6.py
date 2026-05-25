# 6. Automorphic Number Checker

# A digital security company designs smart lockers that open only for special self-matching numeric codes.
# When a user enters a number, the system squares the number and checks whether the result
# ends with the same digits as the original code. If yes, the locker grants access.

# An automorphic number is a number whose square ends with the same number.

# Example:
# 25² = 625

# Write a program using loops to check whether the entered number is an Automorphic number.

# Input:
# 25

# Output:
# Automorphic Number


n=67
automorphic=n**2
print(n)
print(automorphic)

while n>0:
    last1=n%10
    break
while automorphic>0:
    last2=automorphic%10
    break

if last1==last2:
    print("automorphic")
else:
    print("not automorphixc h ")    

















'''
n = int(input())

square = n * n
temp_n = n
temp_sq = square
is_automorphic = True

while temp_n > 0:
    if temp_n % 10 != temp_sq % 10:
        is_automorphic = False
        break
    temp_n //= 10
    temp_sq //= 10

if is_automorphic:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")


#

# n = int(input())

# square = n * n
# temp_n = n
# temp_sq = square
# is_automorphic = True

# for _ in str(n):
#     if temp_n % 10 != temp_sq % 10:
#         is_automorphic = False
#         break
#     temp_n //= 10
#     temp_sq //= 10

# if is_automorphic:
#     print("Automorphic Number")
# else:
#     print("Not an Automorphic Number")
'''