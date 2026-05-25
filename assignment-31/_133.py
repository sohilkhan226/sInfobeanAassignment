# Q133: Convert a Roman numeral string to integer.
# Input: S = "XIV"
# Output: 14
S = "XIV"
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0
for i in range(len(S)):
    if i + 1 < len(S) and roman[S[i]] < roman[S[i + 1]]:
        result -= roman[S[i]]
    else:
        result += roman[S[i]]
print(result)