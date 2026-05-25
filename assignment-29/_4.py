# 4.

# Find All Characters with Maximum Frequency
# Website Traffic Analysis System

# A web analytics company tracks user activity symbols in server logs.

# The company wants to identify all characters having the maximum frequency in the given string.

# Input:
# aabbbccddd
# Output:
# b d

text = input("Enter string: ")

freq = {}

for ch in text:
    if ch != " ":
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

max_freq = 0
for ch in freq:
    if freq[ch] > max_freq:
        max_freq = freq[ch]

result = ""
for ch in freq:
    if freq[ch] == max_freq:
        result += ch + " "

print("Max frequency characters:", result.strip())
