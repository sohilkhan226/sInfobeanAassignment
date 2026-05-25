# Q85: Convert string into a char array without built-in functions.
# Input: S = "test"
# Output: ['t', 'e', 's', 't']
S = "test"
char_array = []
for i in range(len(S)):
    char_array.append(S[i])
print(char_array)

