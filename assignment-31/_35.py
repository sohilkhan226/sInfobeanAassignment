# Q35: Find the first word that is a palindrome.
# Input: S = "this madam is here"
# Output: "madam"
S = "this madam is here"
words = S.split()
result = None
for w in words:
    if w == w[::-1]:
        result = w
        break
print(result)

