# Q32: Count frequency of each word.
# Input: S = "apple banana apple"
# Output: apple: 2, banana: 1
S = "apple banana apple"
words = S.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
for w, c in freq.items():
    print(f"{w}: {c}")





