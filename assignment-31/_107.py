# Q107: Check if a string is a pangram.
# Input: S = "The quick brown fox jumps over the lazy dog"
# Output: True
S = "The quick brown fox jumps over the lazy dog"
alphabet = set("abcdefghijklmnopqrstuvwxyz")
found = set()
for c in S.lower():
    if c in alphabet:
        found.add(c)
print(found == alphabet)