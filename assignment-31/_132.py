# Q132: Check if a string is a valid IP address.
# Input: S = "192.168.1.1"
# Output: True
S = "192.168.1.1"
parts = S.split('.')
valid = True
if len(parts) != 4:
    valid = False
else:
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            valid = False
            break
print(valid)



