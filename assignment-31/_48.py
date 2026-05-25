


# Q48: Remove all vowels.
# Input: S = "aeiou XYZ"
# Output: " XYZ"
S = "aeiou XYZ"
vowels = "aeiouAEIOU"
result = ""
for c in S:
    if c not in vowels:
        result += c
print(result)








