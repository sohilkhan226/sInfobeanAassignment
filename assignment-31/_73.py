# Q73: Find the longest palindromic substring.
# Input: S = "babad"
# Output: "bab"
S = "babad"
longest = ""
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        sub = S[i:j]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub
print(longest)