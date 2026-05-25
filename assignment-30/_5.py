# # 5. Social Media Hashtag Trend Window

# A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

# ### Input:

# ```text
# aabcbcdbca
# ```

# ### Output:

# ```text
# dbca
# ```

# ### Explanation:

# `dbca` contains all unique characters: a,b,c,d

# ---


text = input()

unique_chars = ""
for ch in text:
    if ch not in unique_chars:
        unique_chars += ch

smallest = text

for i in range(len(text)):
    for j in range(i + len(unique_chars), len(text) + 1):
        sub = text[i:j]
        valid = True
        
        for ch in unique_chars:
            if ch not in sub:
                valid = False
                break
        
        if valid and len(sub) < len(smallest):
            smallest = sub

print(smallest)