


# Q7: Convert a string to lowercase.
# Input: S = "HELLO"
# Output: "hello"
S = "HELLO"
result = ""
for char in S:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
print(result)