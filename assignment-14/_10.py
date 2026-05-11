# 10.
# Lift Mode Operation – Advanced Smart Elevator System

# A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
# The system must automatically execute floor movement instructions using loops.

# Write a program:

# - If mode = 1  
#   Normal Up Mode activated.  
#   Read current floor and destination floor.  
#   Print all floors from current to destination in ascending order.

# - Else if mode = 2  
#   Down Mode activated.  
#   Read current floor and destination floor.  
#   Print all floors from current to destination in descending order.

# - Else if mode = 3  
#   Energy Saving Mode activated.  
#   Read destination floor.  
#   Lift starts from ground floor (0) and stops only on alternate floors till destination.

# - Else  
#   Emergency Mode activated.  
#   Print "Emergency Alarm" 4 times using loop.

# Input:
# 3
# 6

# Output:
# 0 2 4 6


# Input:
# 1
# 2
# 7

# Output:
# 2 3 4 5 6 7


# Input:
# 2
# 8
# 3

# Output:
# 8 7 6 5 4 3


# Input:
# 5

# Output:
# Emergency Alarm
# Emergency Alarm
# Emergency Alarm
# Emergency Alarm


mode = int(input())

if mode == 1:
    curr = int(input())
    dest = int(input())
    i = curr
    while i <= dest:
        print(i, end=" ")
        i += 1
    print()

elif mode == 2:
    curr = int(input())
    dest = int(input())
    i = curr
    while i >= dest:
        print(i, end=" ")
        i -= 1
    print()

elif mode == 3:
    dest = int(input())
    i = 0
    while i <= dest:
        print(i, end=" ")
        i += 2
    print()

else:
    i = 0
    while i < 4:
        print("Emergency Alarm")
        i += 1

#



# mode = int(input())

# if mode == 1:
#     curr = int(input())
#     dest = int(input())
#     for i in range(curr, dest + 1):
#         print(i, end=" ")
#     print()

# elif mode == 2:
#     curr = int(input())
#     dest = int(input())
#     for i in range(curr, dest - 1, -1):
#         print(i, end=" ")
#     print()

# elif mode == 3:
#     dest = int(input())
#     for i in range(0, dest + 1, 2):
#         print(i, end=" ")
#     print()

# else:
#     for _ in range(4):
#         print("Emergency Alarm")