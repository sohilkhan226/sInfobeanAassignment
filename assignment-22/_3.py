# 3)	WAP to find out all the leap years between two entered years

start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

print("Leap Years:")

year = start
while year <= end:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
    year += 1