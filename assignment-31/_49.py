# Q49: Replace all consonants with ''.
# Input: S = "apple"
# Output: "ae"
S = "apple"
vowels = "aeiouAEIOU"
result = ""
for c in S:
    if c.isalpha() and c not in vowels:
        result += ""
    else:
        result += c
print(result)