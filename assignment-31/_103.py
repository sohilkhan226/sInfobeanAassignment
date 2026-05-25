# Q103: Check if a string contains balanced parentheses.
# Input: S = "((()))"
# Output: True
S = "((()))"
count = 0
balanced = True
for c in S:
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1
    if count < 0:
        balanced = False
        break
if count != 0:
    balanced = False
print(balanced)




















