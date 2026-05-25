# Q129: Find the smallest window containing all distinct characters.
# Input: S = "aabcbde"
# Output: "abcbde"
S = "aabcbde"
distinct = len(set(S))
freq = {}
start = 0
best = S
for end in range(len(S)):
    freq[S[end]] = freq.get(S[end], 0) + 1
    while len(freq) == distinct:
        window = S[start:end + 1]
        if len(window) <= len(best):
            best = window
        freq[S[start]] -= 1
        if freq[S[start]] == 0:
            del freq[S[start]]
        start += 1
print(best)




