# Q141: Implement Rabin-Karp algorithm for substring search.
# Input: Text = "abcxabc", Pattern = "abc"
# Output: [0, 4]
Text = "abcxabc"
Pattern = "abc"
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1, q)
    p_hash = 0
    t_hash = 0
    result = []
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                result.append(i)
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
    return result
print(rabin_karp(Text, Pattern))


