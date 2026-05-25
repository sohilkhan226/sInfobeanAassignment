# Q127: Group words that are anagrams from an array of strings.
# Input: Arr = ["eat", "tea", "tan", "ate", "nat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"]]
arr = ["eat", "tea", "tan", "ate", "nat"]
groups = {}
for word in arr:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
print(list(groups.values()))
