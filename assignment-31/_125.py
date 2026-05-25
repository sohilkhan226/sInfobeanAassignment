# Q125: Find the shortest common supersequence of two strings.
# Input: S1 = "AGGTAB", S2 = "GXTXAYB"
# Output: "AGGXTXAYB"
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
lcs_str = dp[m][n]
result = ""
i = 0
j = 0
k = 0
while k < len(lcs_str):
    while i < m and S1[i] != lcs_str[k]:
        result += S1[i]
        i += 1
    while j < n and S2[j] != lcs_str[k]:
        result += S2[j]
        j += 1
    result += lcs_str[k]
    i += 1
    j += 1
    k += 1
result += S1[i:] + S2[j:]
print(result)








