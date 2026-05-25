# Q15: Find the last occurrence of a character.
# Input: S = "banana", Char = 'a'
# Output: 5
S = "banana"
char = 'a'
result = -1
for i in range(len(S)):
    if S[i] == char:
        result = i
print(result)