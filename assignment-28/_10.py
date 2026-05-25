# write a program to find number unique charcter in string

text = input("Enter string: ").lower()

unique = ""

for ch in text:
    if ch not in unique:
        unique += ch

print("Number of unique characters:", len(unique))