# Q38: Reverse words without using split().
# Input: S = "a b c"
# Output: "c b a"
S = "a b c"
word = ""
words_list = []
for c in S:
    if c == ' ':
        if word:
            words_list.append(word)
        word = ""
    else:
        word += c
if word:
    words_list.append(word)
result = ""
for i in range(len(words_list) - 1, -1, -1):
    result += words_list[i]
    if i > 0:
        result += " "
print(result)
