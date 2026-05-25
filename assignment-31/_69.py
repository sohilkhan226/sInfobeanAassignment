# Q69: Count how many times 'life' appears in a string.
# Input: S = "life is life"
# Output: 2
S = "life is life"
words = S.split()
count = 0
for w in words:
    if w == "life":
        count += 1
print(count)