# Q43: Check if two strings are rotations of each other.
# Input: S1 = "abcde", S2 = "cdeab"
# Output: True
S1 = "abcde"
S2 = "cdeab"
if len(S1) == len(S2):
    combined = S1 + S1
    found = False
    for i in range(len(combined) - len(S2) + 1):
        match = True
        for j in range(len(S2)):
            if combined[i + j] != S2[j]:
                match = False
                break
        if match:
            found = True
            break
    print(found)
else:
    print(False)
