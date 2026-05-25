# Q57: Merge two strings alternatively (char by char).
# Input: S1 = "ABC", S2 = "def"
# Output: "AdBeCf"
S1 = "ABC"
S2 = "def"
result = ""
i = 0
while i < len(S1) or i < len(S2):
    if i < len(S1):
        result += S1[i]
    if i < len(S2):
        result += S2[i]
    i += 1
print(result)