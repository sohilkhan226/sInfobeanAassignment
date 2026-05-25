# 2.
# Fibonacci Series Generator

# A learning app helps students understand number patterns. One of the most important patterns is the Fibonacci series, where each number is the sum of the previous two numbers.

# The series starts with:
# 0 1

# Write a program to:

# - Read a number n (number of terms)
# - Print the Fibonacci series up to n terms using a loop

# Input:
# 7

# Output:
# 0 1 1 2 3 5 8

n=10
a=0
b=1
for i in range(n):
    print(a)
    temp=a+b
    a=b
    b=temp
    


'''
n = int(input())

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

n = int(input())

a, b = 0, 1
count = 0
#

# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1

# print()
'''