# Q105: Find the longest valid parentheses substring.
# Input: S = "()(())"
# Output: 6
S = "()(())"
stack = [-1]
max_len = 0
for i in range(len(S)):
    if S[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            max_len = max(max_len, i - stack[-1])
print(max_len)





