# Q80: Print list items containing all characters of a given word.
# Input: List = ["apple", "plea"], Word = "pal"
# Output: "apple", "plea"
lst = ["apple", "plea"]
word = "pal"
result = []
for item in lst:
    all_found = True
    for c in word:
        if c not in item:
            all_found = False
            break
    if all_found:
        result.append(item)
print(result)
















