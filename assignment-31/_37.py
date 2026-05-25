


# Q37: Reverse each word in a string.
# Input: S = "cat dog"
# Output: "tac god"
S = "cat dog"
words = S.split()
result = " ".join(w[::-1] for w in words)
print(result)