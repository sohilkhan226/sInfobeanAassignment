# Q151: Find the lexicographically previous permutation of a string.
# Input: S = "acb"
# Output: "abc"
S = "acb"
s = list(S)
n = len(s)
i = n - 2
while i >= 0 and s[i] <= s[i + 1]:
    i -= 1
if i >= 0:
    j = n - 1
    while s[j] >= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
s[i + 1:] = reversed(s[i + 1:])
print("".join(s))