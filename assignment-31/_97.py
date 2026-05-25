# Q97: Check if two given strings appear at the end of each other (ignoring case).
# Input: S1 = "abc", S2 = "Xabc"
# Output: True
S1 = "abc"
S2 = "Xabc"
s1_lower = S1.lower()
s2_lower = S2.lower()
result = s2_lower.endswith(s1_lower) or s1_lower.endswith(s2_lower)
print(result)