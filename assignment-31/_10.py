# Q10: Trim leading, trailing, or extra spaces.
# Input: S = "  hello  world  "
# Output: "hello world"
S = "  hello  world  "
words = S.split()
result = " ".join(words)
print(result)