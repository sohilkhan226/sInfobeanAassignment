# Q144: Check if a string is valid HTML/XML tag sequence.
# Input: S = "<a><b></a></b>"
# Output: False
S = "<a><b></a></b>"
stack = []
i = 0
valid = True
while i < len(S):
    if S[i] == '<':
        j = S.index('>', i)
        tag = S[i + 1:j]
        if tag.startswith('/'):
            if not stack or stack[-1] != tag[1:]:
                valid = False
                break
            stack.pop()
        else:
            stack.append(tag)
        i = j + 1
    else:
        i += 1
if stack:
    valid = False
print(valid)










