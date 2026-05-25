

# Q39: Search all occurrences of a character.
# Input: S = "banana", Char = 'a'
# Output: 1, 3, 5
S = "banana"
char = 'a'
indices = []
for i in range(len(S)):
    if S[i] == char:
        indices.append(i)
print(indices)


