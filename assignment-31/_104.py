#Q104: Check if a string contains balanced brackets of all types.
# Input: S = "{[()]}"
# Output: True
S = "{[()]}"
stack = []
mapping = {')': '(', '}': '{', ']': '['}
balanced = True
for c in S:
    if c in '({[':
        stack.append(c)
    elif c in ')}]':
        if not stack or stack[-1] != mapping[c]:
            balanced = False
            break
        stack.pop()
if stack:
    balanced = False
print(balanced)

