# Q51: Extract only digits.
# Input: S = "a1b2c3"
# Output: "123"
S = "a1b2c3"
result = ""
for c in S:
    if c.isdigit():
        result += c
print(result)