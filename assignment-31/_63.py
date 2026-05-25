# Q63: Count frequency of each character.
# Input: S = "aabcc"
# Output: a: 2, b: 1, c: 2
S = "aabcc"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
for c, count in freq.items():
    print(f"{c}: {count}")