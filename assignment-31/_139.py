# Q139: Check if a string can be segmented into valid dictionary words.
# Input: S = "applepenapple", Dict = ["apple", "pen"]
# Output: True
S = "applepenapple"
dictionary = {"apple", "pen"}
n = len(S)
dp = [False] * (n + 1)
dp[0] = True
for i in range(1, n + 1):
    for j in range(i):
        if dp[j] and S[j:i] in dictionary:
            dp[i] = True
            break
print(dp[n])