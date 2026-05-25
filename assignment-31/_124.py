# Q124: Find the longest common subsequence of two strings.
# Input: S1 = "AGGTAB", S2 = "GXTXAYB"
# Output: "GTAB"
S1 = "AGGTAB"
S2 = "GXTXAYB"
m = len(S1)
n = len(S2)
dp = [[""] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if S1[i - 1] == S2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + S1[i - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
print(dp[m][n])


