# Q74: Find the longest substring without repeating characters.
# Input: S = "abcabcbb"
# Output: "abc"
S = "abcabcbb"
start = 0
max_len = 0
max_sub = ""
char_index = {}
for end in range(len(S)):
    if S[end] in char_index and char_index[S[end]] >= start:
        start = char_index[S[end]] + 1
    char_index[S[end]] = end
    if end - start + 1 > max_len:
        max_len = end - start + 1
        max_sub = S[start:end + 1]
print(max_sub)

