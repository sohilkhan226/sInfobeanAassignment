# Q78: Find the longest mirror-image substring at both ends.
# Input: S = "aabccbaa"
# Output: "aab"
S = "aabccbaa"
result = ""
for length in range(1, len(S) // 2 + 1):
    if S[:length] == S[len(S) - length:][::-1]:
        result = S[:length]
print(result)