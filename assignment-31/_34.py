


# Q34: Find the shortest word.
# Input: S = "find the shortest word"
# Output: "the"
S = "find the shortest word"
words = S.split()
shortest = words[0]
for w in words:
    if len(w) < len(shortest):
        shortest = w
print(shortest)