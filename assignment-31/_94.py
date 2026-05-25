# Q94: Find the smallest window containing all characters of another string.
# Input: S1 = "ADOBECODEBANC", S2 = "ABC"
# Output: "BANC"
S1 = "ADOBECODEBANC"
S2 = "ABC"
def smallest_window(s1, s2):
    from collections import Counter
    need = Counter(s2)
    missing = len(s2)
    best = ""
    i = 0
    for j in range(len(s1)):
        if need[s1[j]] > 0:
            missing -= 1
        need[s1[j]] -= 1
        while missing == 0:
            window = s1[i:j + 1]
            if not best or len(window) < len(best):
                best = window
            need[s1[i]] += 1
            if need[s1[i]] > 0:
                missing += 1
            i += 1
    return best
print(smallest_window(S1, S2))












