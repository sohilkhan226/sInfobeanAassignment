# Q18: Replace occurrences of a character.
# Input: S = "apple", Old='p', New='x'
# Output: "axxle"
S = "apple"
old = 'p'
new = 'x'
result = ""
for c in S:
    if c == old:
        result += new
    else:
        result += c
print(result)