# Q53: Remove all punctuation characters.
# Input: S = "Hello, world!"
# Output: "Hello world"
S = "Hello, world!"
import string
result = ""
for c in S:
    if c not in string.punctuation:
        result += c
print(result)