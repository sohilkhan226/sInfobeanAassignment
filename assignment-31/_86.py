# Q86: Print all permutations of a string without repetition.
# Input: S = "ab"
# Output: "ab", "ba"
S = "ab"
def permutations(s, left, right, result):
    if left == right:
        result.append("".join(s))
        return
    seen = set()
    for i in range(left, right + 1):
        if s[i] not in seen:
            seen.add(s[i])
            s[left], s[i] = s[i], s[left]
            permutations(s, left + 1, right, result)
            s[left], s[i] = s[i], s[left]
result = []
permutations(list(S), 0, len(S) - 1, result)
print(result)