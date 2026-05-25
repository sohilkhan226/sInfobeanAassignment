# Q67: Count how many times a substring appears.
# Input: S = "abab", Sub = "ab"
# Output: 2
S = "abab"
sub = "ab"
count = 0
for i in range(len(S) - len(sub) + 1):
    if S[i:i + len(sub)] == sub:
        count += 1
print(count)