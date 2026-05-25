# Q135: Check if two strings differ by exactly one character.
# Input: S1 = "pale", S2 = "ple"
# Output: False
S1 = "pale"
S2 = "ple"
if len(S1) != len(S2):
    print(False)
else:
    diff = 0
    for i in range(len(S1)):
        if S1[i] != S2[i]:
            diff += 1
    print(diff == 1)