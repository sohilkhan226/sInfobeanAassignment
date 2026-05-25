# Q109: Find the lexicographically smallest substring of length k.
# Input: S = "banana", k = 3
# Output: "ana"
S = "banana"
k = 3
smallest = S[:k]
for i in range(1, len(S) - k + 1):
    sub = S[i:i + k]
    if sub < smallest:
        smallest = sub
print(smallest)