# Q30: Replace a word with another word.
# Input: S = "old data", Old="old", New="new"
# Output: "new data"
S = "old data"
old = "old"
new = "new"
words = S.split()
result = " ".join(new if w == old else w for w in words)
print(result)