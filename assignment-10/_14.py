# 14.Floor Movement System (Elevator)
# An elevator system takes the current floor and destination floor as input.

# If current floor < destination → move upward and display floors
# If current floor > destination → move downward and display floors
# If both are same → display "Already on the same floor"

# Write a program using if-elif-else and loops to simulate elevator movement.

# Input: 1, 5
# Output: 1 → 2 → 3 → 4 → 5

# Input: 7, 3
# Output: 7 → 6 → 5 → 4 → 3

# Input: 4, 4
# Output: Already on the same floor

current     = int(input("Enter current floor: "))
destination = int(input("Enter destination floor: "))

if current < destination:
    i = current
    while i <= destination:
        if i == destination:
            print(i)
        else:
            print(i, end = " → ")
        i = i + 1
elif current > destination:
    i = current
    while i >= destination:
        if i == destination:
            print(i)
        else:
            print(i, end = " → ")
        i = i - 1
else:
    print("Already on the same floor")


# 

# current = int(input("Enter current floor: "))
# destination = int(input("Enter destination floor: "))

# if current < destination:
#     for i in range(current, destination + 1):
#         if i == destination:
#             print(i)
#         else:
#             print(i, end=" → ")

# elif current > destination:
#     for i in range(current, destination - 1, -1):
#         if i == destination:
#             print(i)
#         else:
#             print(i, end=" → ")

# else:
#     print("Already on the same floor")