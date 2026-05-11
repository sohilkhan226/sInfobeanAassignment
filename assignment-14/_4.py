# 4.Unique Digit Security Scanner

# A smart locker accepts only numbers whose all digits are unique.

# Write a program using for-else loop to:

# - Check every digit
# - If any repeated digit found reject
# - Else accept

# Input:
# 57294

# Output:
# Valid Unique Code

num_str = input()
seen = []

for digit in num_str:
    if digit in seen:
        print("Rejected")
        break
    seen.append(digit)
else:  # Executes only if loop finishes without break
    print("Valid Unique Code")




#


# num_str = input()
# seen = []
# i = 0
# repeated = False

# while i < len(num_str):
#     digit = num_str[i]
#     if digit in seen:
#         print("Rejected")
#         repeated = True
#         break
#     seen.append(digit)
#     i += 1

# if not repeated:
#     print("Valid Unique Code")