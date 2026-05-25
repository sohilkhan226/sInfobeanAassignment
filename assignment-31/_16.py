# Q16: Count total occurrences of a character.
# Input: S = "programming", Char = 'g'
# Output: 2
S = "programming"
char = 'g'
count = 0
for c in S:
    if c == char:
        count += 1
print(count)