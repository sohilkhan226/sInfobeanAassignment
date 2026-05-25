


# Q31: Remove duplicate words.
# Input: S = "the cat and the dog"
# Output: "the cat and dog"
S = "the cat and the dog"
words = S.split()
seen = set()
result = []
for w in words:
    if w not in seen:
        result.append(w)
        seen.add(w)
print(" ".join(result))


