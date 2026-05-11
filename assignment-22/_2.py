# 2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N

n = int(input("Enter N: "))

print("Number\tSquare\tCube\tSquare Root")

i = 1
while i <= n:
    print(i, "\t", i**2, "\t", i**3, "\t", round(i**0.5, 2))
    i += 1