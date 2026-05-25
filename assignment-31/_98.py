# Q98: Check if the first 'z' is immediately followed by another 'z'.
# Input: S1 = "zzyy", S2 = "zyzz"
# Output: S1: True, S2: False
S1 = "zzyy"
S2 = "zyzz"
def first_z_followed(s):
    for i in range(len(s) - 1):
        if s[i] == 'z':
            return s[i + 1] == 'z'
    return False
print("S1:", first_z_followed(S1))
print("S2:", first_z_followed(S2))
