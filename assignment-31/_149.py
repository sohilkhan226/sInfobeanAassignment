# Q149: Check if two strings are scrambled versions of each other.
# Input: S1 = "great", S2 = "rgeat"
# Output: True
S1 = "great"
S2 = "rgeat"
memo = {}
def is_scramble(s1, s2):
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    if s1 == s2:
        memo[(s1, s2)] = True
        return True
    if sorted(s1) != sorted(s2):
        memo[(s1, s2)] = False
        return False
    n = len(s1)
    for i in range(1, n):
        if (is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:])) or \
           (is_scramble(s1[:i], s2[n - i:]) and is_scramble(s1[i:], s2[:n - i])):
            memo[(s1, s2)] = True
            return True
    memo[(s1, s2)] = False
    return False
print(is_scramble(S1, S2))





