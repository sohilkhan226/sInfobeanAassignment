
# Q68: Count the sum of digits present in a string.
# Input: S = "a1b2c3"
# Output: 6
S = "a1b2c3"
total = 0
for c in S:
    if c.isdigit():
        total += int(c)
print(total)