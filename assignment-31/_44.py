
# Q44: Check if two strings are anagrams.
# Input: S1 = "listen", S2 = "silent"
# Output: True
S1 = "listen"
S2 = "silent"
freq1 = {}
freq2 = {}
for c in S1:
    freq1[c] = freq1.get(c, 0) + 1
for c in S2:
    freq2[c] = freq2.get(c, 0) + 1
print(freq1 == freq2)