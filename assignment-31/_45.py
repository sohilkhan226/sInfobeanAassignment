# Q45: Check whether a string starts with or ends with another string.
# Input: S = "apple pie", Prefix = "apple", Suffix = "pie"
# Output: Start: True, End: True
S = "apple pie"
prefix = "apple"
suffix = "pie"
starts = S[:len(prefix)] == prefix
ends = S[len(S) - len(suffix):] == suffix
print("Start:", starts)
print("End:", ends)