


# Q46: Check if a substring appears at both the start and end.
# Input: S = "abcabca", Sub = "abca"
# Output: True
S = "abcabca"
sub = "abca"
starts = S[:len(sub)] == sub
ends = S[len(S) - len(sub):] == sub
print(starts and ends)
