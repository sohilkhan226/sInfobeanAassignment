# Q121: Check if a string contains only binary digits (0/1).
# Input: S1 = "1010", S2 = "102"
# Output: S1: True, S2: False
S1 = "1010"
S2 = "102"
def is_binary(s):
    for c in s:
        if c != '0' and c != '1':
            return False
    return True
print("S1:", is_binary(S1))
print("S2:", is_binary(S2))

