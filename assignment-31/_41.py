


# Q41: Check if a string contains a substring (without using built-in method).
# Input: S1 = "Hello", Sub = "ell"
# Output: True
S1 = "Hello"
sub = "ell"
found = False
for i in range(len(S1) - len(sub) + 1):
    match = True
    for j in range(len(sub)):
        if S1[i + j] != sub[j]:
            match = False
            break
    if match:
        found = True
        break
print(found)








