#Q83: Create a string from a byte array.
# Input: Byte[] = [72, 101, 108]
# Output: "Hel"
byte_arr = [72, 101, 108]
result = ""
for b in byte_arr:
    result += chr(b)
print(result)
