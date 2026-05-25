# # 6. AI Chat Toxic Pattern Detector

# An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

# If found:

# ```text
# Spam Pattern Found
# ```

# Else:

# ```text
# Clean Message
# ```

# ### Input:

# ```text
# heyyy broooo welcome
# ```

# ### Output:

# ```text
# Spam Pattern Found
# ```

# ---



text = input()

found = False

for i in range(len(text) - 2):
    if text[i] == text[i+1] == text[i+2]:
        found = True
        break

if found:
    print("Spam Pattern Found")
else:
    print("Clean Message")