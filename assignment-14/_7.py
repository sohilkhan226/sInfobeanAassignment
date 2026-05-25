# 7.
#  Alternate Digit Prime Checker

# A math lab adds alternate digits from right side.

# Write a program to:

# - Find sum of alternate digits
# - Check whether sum is Prime or Not

# Input:
# 12345

# Output:
# Alternate Sum = 9
# Not Prime



sum=0
n=12345
k=0
for i in str(n):
    sum+=int(i)
    i+=2
print(sum)
    



























n = int(input())
temp = n
alt_sum = 0
pos = 0

while temp > 0:
    if pos % 2 == 0:  # 0, 2, 4... from right side
        alt_sum += temp % 10
    temp //= 10
    pos += 1

print("Alternate Sum =", alt_sum)

# Prime check
is_prime = True
if alt_sum <= 1:
    is_prime = False
else:
    i = 2
    while i * i <= alt_sum:
        if alt_sum % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")


#


# n = int(input())
# temp = n
# alt_sum = 0
# pos = 0

# for _ in str(n):
#     if pos % 2 == 0:
#         alt_sum += temp % 10
#     temp //= 10
#     pos += 1

# print("Alternate Sum =", alt_sum)

# # Prime check
# is_prime = True
# if alt_sum <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(alt_sum ** 0.5) + 1):
#         if alt_sum % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")