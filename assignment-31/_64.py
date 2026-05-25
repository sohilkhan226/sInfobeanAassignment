# Q64: Count frequency of each vowel.
# Input: S = "programming"
# Output: a: 1, e: 0, i: 1, o: 1, u: 0
S = "programming"
vowels = "aeiou"
freq = {}
for v in vowels:
    freq[v] = 0
for c in S.lower():
    if c in freq:
        freq[c] += 1
for v, count in freq.items():
    print(f"{v}: {count}")