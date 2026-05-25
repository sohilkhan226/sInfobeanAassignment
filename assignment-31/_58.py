# Q58: Rotate characters by 2 positions to the left.
# Input: S = "abcde"
# Output: "cdeab"
S = "abcde"
n = 2
result = S[n:] + S[:n]
print(result)
