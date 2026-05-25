# Q110: Find the lexicographically largest substring of length k.
# Input: S = "banana", k = 3
# Output: "nan"
S = "banana"
k = 3
largest = S[:k]
for i in range(1, len(S) - k + 1):
    sub = S[i:i + k]
    if sub > largest:
        largest = sub
print(largest)