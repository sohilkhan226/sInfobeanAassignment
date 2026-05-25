# Q20: Find the lowest frequency character.
# Input: S = "aabbcde"
# Output: 'c', 'd', 'e'
S = "aabbcde"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
min_freq = min(freq.values())
result = [c for c in freq if freq[c] == min_freq]
print(result)