# Q65: Count palindromic substrings.
# Input: S = "aaa"
# Output: 6
S = "aaa"
count = 0
n = len(S)
for i in range(n):
    for j in range(i + 1, n + 1):
        sub = S[i:j]
        if sub == sub[::-1]:
            count += 1
print(count)