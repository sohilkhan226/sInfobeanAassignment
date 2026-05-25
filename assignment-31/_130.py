# Q130: Find the maximum occurring word.
# Input: S = "a b a c a"
# Output: 'a'
S = "a b a c a"
words = S.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
max_word = ""
max_count = 0
for w, c in freq.items():
    if c > max_count:
        max_count = c
        max_word = w
print(max_word)





