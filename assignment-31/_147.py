# Q147: Decompress a run-length encoded string.
# Input: S = "a3b2c1"
# Output: "aaabbc"
S = "a3b2c1"
result = ""
i = 0
while i < len(S):
    char = S[i]
    i += 1
    num = ""
    while i < len(S) and S[i].isdigit():
        num += S[i]
        i += 1
    result += char * int(num)
print(result)
