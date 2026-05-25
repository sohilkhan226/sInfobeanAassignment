# Q95: Find the second most frequent character.
# Input: S = "aabbccdde"
# Output: 'c' or 'd'
S = "aabbccdde"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
sorted_chars = sorted(freq, key=freq.get, reverse=True)
print(sorted_chars[1])

