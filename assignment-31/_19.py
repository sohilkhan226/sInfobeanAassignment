


# Q19: Find the highest frequency character.
# Input: S = "abracadabra"
# Output: 'a'
S = "abracadabra"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
max_char = max(freq, key=freq.get)
print(max_char)


