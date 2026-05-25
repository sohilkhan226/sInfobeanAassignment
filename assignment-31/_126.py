# Q126: Print all anagrams of a string.
# Input: S = "cat"
# Output: "act", "atc", "cat", "cta", "tac", "tca"
S = "cat"
def get_perms(s, left, right, result):
    if left == right:
        result.append("".join(s))
        return
    seen = set()
    for i in range(left, right + 1):
        if s[i] not in seen:
            seen.add(s[i])
            s[left], s[i] = s[i], s[left]
            get_perms(s, left + 1, right, result)
            s[left], s[i] = s[i], s[left]
result = []
get_perms(list(S), 0, len(S) - 1, result)
print(sorted(result))

