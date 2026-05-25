


# Q17: Remove occurrences of a character.
# Input: S = "banana", Char = 'a', Remove All
# Output: "bnn"
S = "banana"
char = 'a'
result = ""
for c in S:
    if c != char:
        result += c
print(result)