# Q72: Print all substrings of length n.
# Input: S = "abc", n = 2
# Output: "ab", "bc"
S = "abc"
n = 2
result = []
for i in range(len(S) - n + 1):
    result.append(S[i:i + n])
print(result)