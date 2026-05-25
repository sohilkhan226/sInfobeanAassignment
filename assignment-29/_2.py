# 2.
# Find the Most Frequently Occurring Word
# News Channel Keyword Analyzer

# A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

# Write a Python program to find the word with the highest frequency.

# Input:
# india won the match and india created history
# Output:
# india


sentence = input("Enter sentence: ")

words = []
word = ""
for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

# Count frequency
freq_words = []
freq_count = []

for w in words:
    found = False
    for i in range(len(freq_words)):
        if freq_words[i] == w:
            freq_count[i] += 1
            found = True
            break
    if not found:
        freq_words.append(w)
        freq_count.append(1)

# Find max
max_count = 0
max_word = ""
for i in range(len(freq_count)):
    if freq_count[i] > max_count:
        max_count = freq_count[i]
        max_word = freq_words[i]

print("Most frequent word:", max_word)