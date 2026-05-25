# 2. Next Prime ID Generator

# A multinational company auto-generates employee IDs in numeric sequence.
#  Due to internal policy, only prime numbered IDs are assigned to new premium employees.

# The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

# Write a program to find the first prime number after n.

# Input:
# 14

# Output:
# Next Prime = 17


n=17
candidate=n+1
flag=True
while True:
    if flag==True:
        for i in range(2,candidate):
            if candidate%i==0:
                flag=True
                break
        else:
            flag=False
    if flag==True:
        candidate+=1
    else:
        print("ye mil gya prime number",candidate)
        break

    
                

    

    

















'''
n = int(input())

candidate = n + 1
while True:
    is_prime = True
    if candidate <= 1:
        is_prime = False
    else:
        i = 2
        while i * i <= candidate:
            if candidate % i == 0:
                is_prime = False
                break
            i += 1
            
    if is_prime:
        print("Next Prime =", candidate)
        break
    candidate += 1

#
# n = int(input())

# candidate = n + 1
# found = False

# while not found:
#     is_prime = True
#     if candidate <= 1:
#         is_prime = False
#     else:
#         for i in range(2, int(candidate**0.5) + 1):
#             if candidate % i == 0:
#                 is_prime = False
#                 break

#     if is_prime:
#         print("Next Prime =", candidate)
#         found = True
#     candidate += 1
'''