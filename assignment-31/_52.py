# Q52: Remove all special characters.
# Input: S = "a!@b#c"
# Output: "abc"
S = "a!@b#c"
result = ""
for c in S:
    if c.isalnum():
        result += c
print(result)