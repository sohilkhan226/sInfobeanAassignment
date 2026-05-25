


# Q21: Find the first non-repeating character.
# Input: S = "aabbcde"
# Output: 'c'
S = "aabbcde"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
result = None
for c in S:
    if freq[c] == 1:
        result = c
        break
print(result)





