# Q14: Find the first occurrence of a character.
# Input: S = "banana", Char = 'a'
# Output: 1
S = "banana"
char = 'a'
result = -1
for i in range(len(S)):
    if S[i] == char:
        result = i
        break
print(result)