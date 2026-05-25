# # 2. AI Auto-Correct Consecutive Word Remover

# An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

# The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

# ### Input:

# ```text
# hello hello hello team meeting meeting started
# ```

# ### Output:

# ```text
# hello team meeting started
# ```

# ---


sentence = input()

words = sentence.split()
result = []

for word in words:
    if len(result) == 0 or word != result[-1]:
        result.append(word)

print(" ".join(result))
