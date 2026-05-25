# Q146: Compress a string using run-length encoding.
# Input: S = "aaabbc"
# Output: "a3b2c1"
S = "aaabbc"
result = ""
i = 0
while i < len(S):
    count = 1
    while i + count < len(S) and S[i + count] == S[i]:
        count += 1
    result += S[i] + str(count)
    i += count
print(result)