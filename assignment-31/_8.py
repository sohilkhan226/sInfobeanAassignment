


# Q8: Toggle the case of each character.
# Input: S = "MiXED"
# Output: "mIxeD"
S = "MiXED"
result = ""
for char in S:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
print(result)








