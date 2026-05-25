# Q55: Reverse only vowels.
# Input: S = "hello"
# Output: "holle"
S = "hello"
vowels = "aeiouAEIOU"
s_list = list(S)
left = 0
right = len(s_list) - 1
while left < right:
    while left < right and s_list[left] not in vowels:
        left += 1
    while left < right and s_list[right] not in vowels:
        right -= 1
    s_list[left], s_list[right] = s_list[right], s_list[left]
    left += 1
    right -= 1
print("".join(s_list))
