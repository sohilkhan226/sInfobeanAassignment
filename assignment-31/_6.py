

# Q6: Convert a string to uppercase.
# Input: S = "hello"
# Output: "HELLO"
S = "hello"
result = ""
for char in S:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char
print(result)