# Q114: Check if one string is a subsequence of another.
# Input: S1 = "ace", S2 = "abcde"
# Output: True
S1 = "ace"
S2 = "abcde"
i = 0
for c in S2:
    if i < len(S1) and c == S1[i]:
        i += 1
print(i == len(S1))