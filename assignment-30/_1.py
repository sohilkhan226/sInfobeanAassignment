# 1. Smart Log File Error Pattern Detector

# A cybersecurity company stores server logs containing repeated system activity characters.

# To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

# If multiple substrings have the same length, print the first one found.

#  Input:

# ```text
# abcabcbb
# ```

# Output:

# ```text
# abc
# ```

# ---

text = input()

longest = ""

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        sub = text[i:j]
        count = 0
        
        for k in range(len(text) - len(sub) + 1):
            if text[k:k+len(sub)] == sub:
                count += 1
        
        if count > 1 and len(sub) > len(longest):
            longest = sub

print(longest)

