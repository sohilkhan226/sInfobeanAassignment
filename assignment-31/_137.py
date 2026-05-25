# Q137: Find the length of the longest substring with at most k distinct characters.
# Input: S = "eceba", k = 2
# Output: 3
S = "eceba"
k = 2
freq = {}
start = 0
max_len = 0
for end in range(len(S)):
    freq[S[end]] = freq.get(S[end], 0) + 1
    while len(freq) > k:
        freq[S[start]] -= 1
        if freq[S[start]] == 0:
            del freq[S[start]]
        start += 1
    if end - start + 1 > max_len:
        max_len = end - start + 1
print(max_len)


