# Q56: Reverse only consonants.
# Input: S = "apple"
# Output: "eplpa"
S = "apple"
vowels = "aeiouAEIOU"
s_list = list(S)
left = 0
right = len(s_list) - 1
while left < right:
    while left < right and (s_list[left] in vowels or not s_list[left].isalpha()):
        left += 1
    while left < right and (s_list[right] in vowels or not s_list[right].isalpha()):
        right -= 1
    s_list[left], s_list[right] = s_list[right], s_list[left]
    left += 1
    right -= 1
print("".join(s_list))

































































