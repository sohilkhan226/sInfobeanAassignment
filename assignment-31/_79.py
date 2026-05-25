# Q79: Divide a string into n equal parts.
# Input: S = "abcdef", n = 3
# Output: "ab", "cd", "ef"
S = "abcdef"
n = 3
part_size = len(S) // n
parts = []
for i in range(0, len(S), part_size):
    parts.append(S[i:i + part_size])
print(parts)