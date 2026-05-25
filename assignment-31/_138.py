# Q138: Find all palindromic partitions of a string.
# Input: S = "aab"
# Output: [["a", "a", "b"], ["aa", "b"]]
S = "aab"
def palindrome_partition(s):
    result = []
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                path.append(sub)
                backtrack(end, path)
                path.pop()
    backtrack(0, [])
    return result
print(palindrome_partition(S))





