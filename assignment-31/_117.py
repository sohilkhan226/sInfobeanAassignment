# Q117: Check if a string contains duplicate substrings.
# Input: S = "ababa"
# Output: True
S = "ababa"
seen = set()
found = False
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        sub = S[i:j]
        if sub in seen:
            found = True
            break
        seen.add(sub)
    if found:
        break
print(found)