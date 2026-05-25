# Q22: Find the last repeating character.
# Input: S = "abracadabra"
# Output: 'r'
S = "abracadabra"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
result = None
for c in S:
    if freq[c] > 1:
        result = c
print(result)