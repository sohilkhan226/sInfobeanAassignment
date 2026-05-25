# Q96: Find the second most frequent word.
# Input: S = "a b a c b"
# Output: 'b'
S = "a b a c b"
words = S.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
sorted_words = sorted(freq, key=freq.get, reverse=True)
print(sorted_words[1])