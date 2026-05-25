# Q101: Check if a string is a valid palindrome ignoring spaces and punctuation.
# Input: S = "A man, a plan, a canal: Panama"
# Output: True
S = "A man, a plan, a canal: Panama"
cleaned = ""
for c in S:
    if c.isalnum():
        cleaned += c.lower()
print(cleaned == cleaned[::-1])