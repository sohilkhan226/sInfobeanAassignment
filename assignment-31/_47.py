# Q47: Check if one string is a substring of another using only concatenation.
# Input: S1 = "CDAB", S2 = "ABCD"
# Output: True
S1 = "CDAB"
S2 = "ABCD"
combined = S2 + S2
found = False
for i in range(len(combined) - len(S1) + 1):
    match = True
    for j in range(len(S1)):
        if combined[i + j] != S1[j]:
            match = False
            break
    if match:
        found = True
        break
print(found)