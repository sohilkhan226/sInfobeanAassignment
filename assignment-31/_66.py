# Q66: Count number of sentences in a paragraph.
# Input: P = "This. Is. Test."
# Output: 3
P = "This. Is. Test."
count = 0
for c in P:
    if c in '.!?':
        count += 1
print(count)