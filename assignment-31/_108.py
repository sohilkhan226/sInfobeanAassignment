# Q108: Check if a string is an isogram.
# Input: S = "ambidextrous"
# Output: True
S = "ambidextrous"
lower = S.lower()
seen = set()
is_isogram = True
for c in lower:
    if c.isalpha():
        if c in seen:
            is_isogram = False
            break
        seen.add(c)
print(is_isogram)