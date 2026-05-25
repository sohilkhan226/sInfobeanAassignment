# Q40: Search all occurrences of a word.
# Input: S = "a b a b", Word = "b"
# Output: 2, 6
S = "a b a b"
word = "b"
indices = []
start = 0
while True:
    pos = S.find(word, start)
    if pos == -1:
        break
    indices.append(pos)
    start = pos + 1
print(indices)