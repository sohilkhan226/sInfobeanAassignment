# write a program to remove duplicate word from string.

text = input("Enter sentence: ")

words = text.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

text = " ".join(unique_words)

print("After removing duplicates:", text)