# Q54: Replace all duplicate characters with '$'.
# Input: S = "hello"
# Output: "he$$o"
S = "hello"
freq = {}
for c in S:
    freq[c] = freq.get(c, 0) + 1
seen = {}
result = ""
for c in S:
    if freq[c] > 1:
        result += '$'
    else:
        result += c
print(result)