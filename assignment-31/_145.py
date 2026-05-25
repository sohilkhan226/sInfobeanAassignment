# Q145: Remove HTML tags from a string.
# Input: S = "<h1>Title</h1>"
# Output: "Title"
S = "<h1>Title</h1>"
result = ""
inside_tag = False
for c in S:
    if c == '<':
        inside_tag = True
    elif c == '>':
        inside_tag = False
    elif not inside_tag:
        result += c
print(result)

