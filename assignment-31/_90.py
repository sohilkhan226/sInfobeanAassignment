# Q90: Remove adjacent duplicates recursively.
# Input: S = "azxxzy"
# Output: "ay"
S = "azxxzy"
def remove_adj_dup(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    new_s = "".join(stack)
    if new_s == s:
        return new_s
    return remove_adj_dup(new_s)
print(remove_adj_dup(S))