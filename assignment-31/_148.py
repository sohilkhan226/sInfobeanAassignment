# Q148: Find the first recurring substring of length k.
# Input: S = "abcab", k = 2
# Output: "ab"
S = "abcab"
k = 2
seen = set()
result = None
for i in range(len(S) - k + 1):
    sub = S[i:i + k]
    if sub in seen:
        result = sub
        break
    seen.add(sub)
print(result)
