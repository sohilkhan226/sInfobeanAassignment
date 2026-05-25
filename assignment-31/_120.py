# Q120: Find the longest substring containing only vowels.
# Input: S = "abaeiouy"
# Output: "aeiou"
S = "abaeiouy"
vowels = "aeiouAEIOU"
max_sub = ""
current = ""
for c in S:
    if c in vowels:
        current += c
        if len(current) > len(max_sub):
            max_sub = current
    else:
        current = ""
print(max_sub)






