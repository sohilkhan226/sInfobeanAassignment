


# Q50: Remove all digits.
# Input: S = "a1b2c3"
# Output: "abc"
S = "a1b2c3"
result = ""
for c in S:
    if not c.isdigit():
        result += c
print(result)








