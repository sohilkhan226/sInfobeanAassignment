# 1. Prime Security Code Checker

# A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
#  only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

# When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

# Write a program to check whether the entered number is Prime or Not Prime.

# Input:
# 29

# Output:
# Prime Number


# n=45
# count=1
# flag=True
# for i in range(2,29):
#     if n%i==0:
#         flag=False
# if(flag==True):
#     print("prime number")
# else:
#     print("not prime number")

for i in range(1,101):
    j=1
    for j in range(2,i+1):
        if i%j==0:
            break
    if i==j:
        print(i,end=" ")
    
            
            
       
        
    















'''
n = int(input())

if n <= 1:
    print("Not Prime Number")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
        
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")
'''






#

# n = int(input())

# if n <= 1:
#     print("Not Prime Number")
# else:
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime Number")
#     else:
#         print("Not Prime Number")







