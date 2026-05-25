# Q89: Remove 'b' and 'ac' from a string.
# Input: S = "abacbb"
# Output: ""
S = "abacbb"
result = ""
i = 0
while i < len(S):
    if S[i] == 'b':
        i += 1
    elif i + 1 < len(S) and S[i] == 'a' and S[i + 1] == 'c':
        i += 2
    else:
        result += S[i]
        i += 1
print(result)