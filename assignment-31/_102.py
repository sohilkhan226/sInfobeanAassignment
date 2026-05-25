# Q102: Reverse a string using recursion.
# Input: S = "abc"
# Output: "cba"
S = "abc"
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]
print(reverse_recursive(S))
