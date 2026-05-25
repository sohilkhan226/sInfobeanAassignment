# Q77: Find the longest substring that appears at both ends.
# Input: S = "abracadabra"
# Output: "abra"
S = "abracadabra"
result = ""
for length in range(1, len(S) // 2 + 1):
    if S[:length] == S[len(S) - length:]:
        result = S[:length]
print(result)
