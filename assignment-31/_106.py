# Q106: Generate all subsequences of a string.
# Input: S = "ab"
# Output: "", "a", "b", "ab"
S = "ab"
result = [""]
for c in S:
    new_subs = []
    for sub in result:
        new_subs.append(sub + c)
    result += new_subs
print(result)

