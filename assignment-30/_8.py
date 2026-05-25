# # 8. Intelligent Search Query Compressor

# A search engine company wants to compress user queries.

# ## Rules:

# * Count frequency of each character
# * Display characters in sorted order
# * Ignore spaces
# * Case insensitive

# ### Input:

# ```text
# Google Search
# ```

# ### Output:

# ```text
# a1c1e2g2h1l1o2r1s1t1
# ```


text = input().lower()

freq = {}

for ch in text:
    if ch != " ":
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

# Sort characters alphabetically
sorted_chars = sorted(freq.keys())

result = ""
for ch in sorted_chars:
    result += ch + str(freq[ch])

print(result)