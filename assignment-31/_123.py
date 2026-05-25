# Q123: Convert a decimal number to binary string.
# Input: N = 5
# Output: "101"
N = 5
if N == 0:
    result = "0"
else:
    result = ""
    n = N
    while n > 0:
        result = str(n % 2) + result
        n //= 2
print(result)


