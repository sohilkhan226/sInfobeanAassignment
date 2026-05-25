# **13. Number Range Display System (if-elif with loops)**
# A number analysis tool processes two input values and displays numbers between them based on their relationship.

# * If the first number is less than the second, display numbers in ascending order
# * If the first number is greater than the second, display numbers in descending order
# * If both numbers are equal, display "Both numbers are same"

# Write a program using **if-elif-else and loops** to implement this logic.

# Input: 5, 10
# Output: 5 6 7 8 9 10

# Input: 10, 5
# Output: 10 9 8 7 6 5

# Input: 7, 7
# Output: Both numbers are same

# ---
a=int(input("enter the number"))
b=int(input("enter the number"))

if a<b:
    for i in range(a,b+1):
        a+=1
        print(a)
elif b>a:
     for i in range(b-1,a-1,-1):
        b-=1
        print(b)
else:
    print("both are equal")











# first  = int(input("Enter first number: "))
# second = int(input("Enter second number: "))

# if first < second:
#     i = first
#     while i <= second:
#         print(i, end = " ")
#         i = i + 1
#     print()
# elif first > second:
#     i = first
#     while i >= second:
#         print(i, end = " ")
#         i = i - 1
#     print()
# else:
#     print("Both numbers are same")

# #
# # first = int(input("Enter first number: "))
# # second = int(input("Enter second number: "))

# # if first < second:
# #     for i in range(first, second + 1):
# #         print(i, end=" ")
# #     print()
# # elif first > second:
# #     for i in range(first, second - 1, -1):
# #         print(i, end=" ")
# #     print()
# # else:
# #     print("Both numbers are same")