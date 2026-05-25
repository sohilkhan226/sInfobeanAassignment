# Q75: Find the longest common prefix among strings.
# Input: Strings = ["flower", "flow", "flight"]
# Output: "fl"
strings = ["flower", "flow", "flight"]
prefix = strings[0]
for s in strings[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break
print(prefix)
