# Q28: Count occurrences of a word.
# Input: S = "word word other word", Word = "word"
# Output: 3
S = "word word other word"
word = "word"
words = S.split()
count = 0
for w in words:
    if w == word:
        count += 1
print(count)