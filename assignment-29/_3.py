# 3.
# Replace Consecutive Duplicate Characters with Single Character
# Data Compression System

# A cloud storage company wants to reduce unnecessary repeated characters in text logs.

# Write a Python program that replaces consecutive duplicate characters with a single occurrence.

# Input:
# aaabbbccccdddaa
# Output:
# abcda


text = input("Enter string: ")

result = ""
i = 0

while i < len(text):
    if i == 0:
        result += text[i]
    else:
        if text[i] != text[i - 1]:
            result += text[i]
    i += 1

print("After compression:", result)