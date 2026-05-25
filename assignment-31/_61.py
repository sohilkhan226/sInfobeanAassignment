# Q61: Count total alphabets, digits, and special characters.
# Input: S = "a1b!c2"
# Output: Alphabets: 3, Digits: 2, Special: 1
S = "a1b!c2"
alpha = 0
digit = 0
special = 0
for c in S:
    if c.isalpha():
        alpha += 1
    elif c.isdigit():
        digit += 1
    else:
        special += 1
print("Alphabets:", alpha)
print("Digits:", digit)
print("Special:", special)