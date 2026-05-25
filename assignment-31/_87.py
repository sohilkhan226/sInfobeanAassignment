# Q87: Print all permutations of a string with repetition.
# Input: S = "aab"
# Output: "aab", "aba", "baa"
S = "aab"
def perm_with_repeat(s, left, right, result):
    if left == right:
        result.append("".join(s))
        return
    seen = set()
    for i in range(left, right + 1):
        if s[i] not in seen:
            seen.add(s[i])
            s[left], s[i] = s[i], s[left]
            perm_with_repeat(s, left + 1, right, result)
            s[left], s[i] = s[i], s[left]
result = []
perm_with_repeat(list(S), 0, len(S) - 1, result)
print(sorted(result))











