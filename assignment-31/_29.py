


# Q29: Remove occurrences of a word.
# Input: S = "a test b test c", Word = "test", Remove All
# Output: "a b c"
S = "a test b test c"
word = "test"
words = S.split()
result = " ".join(w for w in words if w != word)
print(result)


