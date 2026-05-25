# Q62: Count vowels and consonants.
# Input: S = "apple"
# Output: Vowels: 2, Consonants: 3
S = "apple"
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for c in S:
    if c.isalpha():
        if c in vowels:
            v_count += 1
        else:
            c_count += 1
print("Vowels:", v_count)
print("Consonants:", c_count)