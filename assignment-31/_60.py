# Q60: Append two strings but remove duplicate adjacent characters.
# Input: S1 = "miss", S2 = "issippi"
# Output: "misisipi"
S1 = "miss"
S2 = "issippi"
combined = S1 + S2
result = combined[0]
for i in range(1, len(combined)):
    if combined[i] != combined[i - 1]:
        result += combined[i]
print(result)