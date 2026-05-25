# Q140: Implement KMP algorithm for substring search.
# Input: Text = "abcxabc", Pattern = "abc"
# Output: [0, 4]
Text = "abcxabc"
Pattern = "abc"
def kmp_search(text, pattern):
    def build_lps(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    lps = build_lps(pattern)
    result = []
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result
print(kmp_search(Text, Pattern))


