# Q92: Check if two strings are pq-balanced.
# Input: S1 = "pqqp", S2 = "qpqp"
# Output: S1: True, S2: False
S1 = "pqqp"
S2 = "qpqp"
def is_pq_balanced(s):
    count = 0
    for c in s:
        if c == 'p':
            count += 1
        elif c == 'q':
            count -= 1
        if count < 0:
            return False
    return count == 0
print("S1:", is_pq_balanced(S1))
print("S2:", is_pq_balanced(S2))


