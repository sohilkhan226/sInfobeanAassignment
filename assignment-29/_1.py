# 1.
# Find the Longest Substring Without Repeating Characters
# Cybersecurity Session Tracking System

# A cybersecurity company monitors user session IDs generated during secure login sessions.

# To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

# Input:
# abcabcbb
# Output:
# abc

text = input("Enter string: ")

longest = ""
current = ""

i = 0
while i < len(text):
    ch = text[i]

    # Check if ch already exists in current
    found = False
    pos = 0
    for j in range(len(current)):
        if current[j] == ch:
            found = True
            pos = j
            break

    if found:
        # Remove characters up to and including pos
        current = current[pos + 1:]

    current += ch

    if len(current) > len(longest):
        longest = current

    i += 1

print("Longest Substring:", longest)