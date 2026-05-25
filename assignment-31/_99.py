# Q99: Check if a 'z' is happy (surrounded by same chars).
# Input: S = "azzb"
# Output: False
S = "azzb"
def is_z_happy(s):
    for i in range(len(s)):
        if s[i] == 'z':
            if i == 0 or i == len(s) - 1:
                return False
            if s[i - 1] != s[i + 1]:
                return False
    return True
print(is_z_happy(S))