# Q100: Return true if string contains 'abc' not followed by '.'.
# Input: S1 = "abcx", S2 = "abc."
# Output: S1: True, S2: False
S1 = "abcx"
S2 = "abc."
def abc_not_dot(s):
    for i in range(len(s) - 2):
        if s[i:i + 3] == 'abc':
            if i + 3 >= len(s) or s[i + 3] != '.':
                return True
    return False
print("S1:", abc_not_dot(S1))
print("S2:", abc_not_dot(S2))







