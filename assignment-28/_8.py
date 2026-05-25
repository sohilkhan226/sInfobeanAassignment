# 8.
# Find the Second Highest Repeating Character in a String

# Social Media Trend Analysis System

# A social media company analyzes hashtags and user comments to identify trending character patterns.

# The analytics team wants a Python program to find the character with the second highest frequency in a given string.

# This helps detect secondary trending patterns in user activity.

# Input:

# aaabbbbccddeee

# Output:

# e

# Explanation:

# b occurs 4 times → highest
# e occurs 3 times → second highest

# Condition:

# Program should work for both uppercase and lowercase letters.
# Spaces should be ignored.
# If no second highest frequency exists, print:
# Second highest repeating character not found

text = input().lower()

freq = {}

for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

# Find highest and second highest
values = sorted(set(freq.values()), reverse=True)

if len(values) < 2:
    print("Second highest repeating character not found")
else:
    second_highest = values[1]
    for ch in freq:
        if freq[ch] == second_highest:
            print(ch)
            break