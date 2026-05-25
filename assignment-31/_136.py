# Q136: Check if two strings are one edit distance apart.
# Input: S1 = "pale", S2 = "ple"
# Output: True
S1 = "pale"
S2 = "ple"
def one_edit_apart(s1, s2):
    m = len(s1)
    n = len(s2)
    if abs(m - n) > 1:
        return False
    if m > n:
        s1, s2 = s2, s1
        m, n = n, m
    for i in range(m):
        if s1[i] != s2[i]:
            if m == n:
                return s1[i + 1:] == s2[i + 1:]
            else:
                return s1[i:] == s2[i + 1:]
    return m + 1 == n
print(one_edit_apart(S1, S2))


