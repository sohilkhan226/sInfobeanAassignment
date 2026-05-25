


# Q23: Print all characters that occur exactly twice.
# Input: S = "aabbcdee"
# Output: 'a', 'b', 'e'
S = "aabbcdee"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
result = [c for c in freq if freq[c] == 2]
print(result)