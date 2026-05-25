# Q122: Convert a binary string to decimal.
# Input: S = "101"
# Output: 5
S = "101"
result = 0
for bit in S:
    result = result * 2 + int(bit)
print(result)