# Q128: Check if a string follows a given pattern.
# Input: Pattern = "abba", S = "dog cat cat dog"
# Output: True
pattern = "abba"
S = "dog cat cat dog"
words = S.split()
result = True
if len(pattern) != len(words):
    result = False
else:
    p2w = {}
    w2p = {}
    for p, w in zip(pattern, words):
        if p in p2w and p2w[p] != w:
            result = False
            break
        if w in w2p and w2p[w] != p:
            result = False
            break
        p2w[p] = w
        w2p[w] = p
print(result)

