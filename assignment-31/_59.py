# Q59: Rotate characters by 3 positions to the right.
# Input: S = "abcde"
# Output: "cdeab"
S = "abcde"
n = 3
result = S[len(S) - n:] + S[:len(S) - n]
print(result)