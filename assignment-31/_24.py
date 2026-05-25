# Q24: Check if all characters in a string are unique.
# Input: S1 = "abc", S2 = "abca"
# Output: S1: True, S2: False
S1 = "abc"
S2 = "abca"
def all_unique(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True
print("S1:", all_unique(S1))
print("S2:", all_unique(S2))