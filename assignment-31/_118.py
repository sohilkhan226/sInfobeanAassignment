# Q118: Find the longest repeated substring.
# Input: S = "banana"
# Output: "ana"
S = "banana"
n = len(S)
longest = ""
for length in range(n - 1, 0, -1):
    seen = set()
    found = False
    for i in range(n - length + 1):
        sub = S[i:i + length]
        if sub in seen:
            longest = sub
            found = True
            break
        seen.add(sub)
    if found:
        break
print(longest)


