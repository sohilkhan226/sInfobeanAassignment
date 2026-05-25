# Q71: Print all substrings.
# Input: S = "abc"
# Output: a, b, c, ab, bc, abc
S = "abc"
substrings = []
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substrings.append(S[i:j])
print(substrings)