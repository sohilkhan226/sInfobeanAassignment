# 7. Remove Duplicate Words from a String

# Voice Assistant Noise Correction System

# A voice assistant records spoken commands from users.

# Due to microphone disturbance and network lag, some words are repeated multiple times.

# The company wants a Python program that removes duplicate words while maintaining the original order.

# ``
# hello hello how are are you
# ```

# Output:

# ```
# hello how are you
# ```


text = input()

words = text.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print(" ".join(unique_words))