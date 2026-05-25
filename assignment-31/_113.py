# Q113: Find the minimum number of insertions to make a string palindrome.
# Input: S = "aebcbda"
# Output: 2
S = "aebcbda"
n = len(S)
dp = [[0] * n for _ in range(n)]
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if S[i] == S[j]:
            dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
print(dp[0][n - 1])
