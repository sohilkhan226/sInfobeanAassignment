# Q42: Check if two strings are equal without using equals().
# Input: S1 = "abc", S2 = "abc"
# Output: True
S1 = "abc"
S2 = "abc"
equal = True
if len(S1) != len(S2):
    equal = False
else:
    for i in range(len(S1)):
        if S1[i] != S2[i]:
            equal = False
            break
print(equal)


