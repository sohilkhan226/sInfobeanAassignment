# Q33: Find the longest word.
# Input: S = "find the longest word"
# Output: "longest"
S = "find the longest word"
words = S.split()
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)