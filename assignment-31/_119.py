# Q119: Find the smallest substring containing all vowels.
# Input: S = "aeiouy"
# Output: "aeiou"
S = "aeiouy"
vowels = set("aeiou")
best = ""
for i in range(len(S)):
    found_vowels = set()
    for j in range(i, len(S)):
        if S[j] in vowels:
            found_vowels.add(S[j])
        if found_vowels == vowels:
            window = S[i:j + 1]
            if not best or len(window) < len(best):
                best = window
            break
print(best)