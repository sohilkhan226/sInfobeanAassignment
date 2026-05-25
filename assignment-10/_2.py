# 2. Factorial of a Number
# In project scheduling, tasks are dependent on previous tasks, and the total
#number of ways to arrange them is calculated using factorial. Factorial of a number
#n is the product of all numbers from 1 to n.
# Write a program to calculate the **factorial of a given number using loops**.

# Input: n = 5
# Output: Total Ways = 120



n = int(input("Enter n: "))

factorial = 1
i = 1

while i <= n:
    factorial = factorial * i
    i = i + 1

print("Total Ways =", factorial)


n = int(input("Enter n: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Total Ways =", fact)