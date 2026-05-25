# Q93: Match strings with wildcard characters (*, ?).
# Input: Pattern = "a?c", Text = "axcde"
# Output: True
Pattern = "a?c*"
Text = "axcde"
def wildcard_match(pattern, text):
    m = len(pattern)
    n = len(text)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif pattern[i - 1] == '?' or pattern[i - 1] == text[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]
print(wildcard_match(Pattern, Text))


