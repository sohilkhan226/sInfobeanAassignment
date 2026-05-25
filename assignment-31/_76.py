# Q76: Find the longest common suffix among strings.
# Input: Strings = ["baking", "making", "taking"]
# Output: "aking"
strings = ["baking", "making", "taking"]
suffix = strings[0]
for s in strings[1:]:
    while not s.endswith(suffix):
        suffix = suffix[1:]
        if not suffix:
            break
print(suffix)