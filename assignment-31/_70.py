# Q70: Compare the number of times 'the' and 'is' appear.
# Input: S = "the cat is on the mat"
# Output: the: 2, is: 1
S = "the cat is on the mat"
words = S.split()
the_count = 0
is_count = 0
for w in words:
    if w == "the":
        the_count += 1
    elif w == "is":
        is_count += 1
print("the:", the_count)
print("is:", is_count)