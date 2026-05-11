# 1.Leap Year Event Scheduler – Multi-Year Analysis System

# A city event management system schedules special festivals only in leap years.

# To plan future events, the system analyzes multiple years instead of just one.

# Write a program to:

# - Read start year and end year from user
# - For every year in the range, check whether it is a Leap Year or Not 
# - Apply rules:
#     - Divisible by 4 → Leap Year candidate  
#     - Divisible by 100 → Not Leap Year  
#     - Divisible by 400 → Leap Year  

# - If leap year → print year with "Event Scheduled"
# - Else → print year with "No Event"

# - After checking all years:
#     - Count total leap years
#     - Print total events scheduled

# Input:
# 2000
# 2005

# Output:
# 2000 → Event Scheduled
# 2001 → No Event
# 2002 → No Event
# 2003 → No Event
# 2004 → Event Scheduled
# 2005 → No Event

# Total Leap Years = 2
# Total Events Scheduled = 2

start_year = int(input())
end_year = int(input())

leap_count = 0

for year in range(start_year, end_year + 1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} → Event Scheduled")
        leap_count += 1
    else:    .
        print(f"{year} → No Event")

print(f"\nTotal Leap Years = {leap_count}")
print(f"Total Events Scheduled = {leap_count}")

#
# start_year = int(input())
# end_year = int(input())

# leap_count = 0
# year = start_year

# while year <= end_year:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print(str(year) + " → Event Scheduled")
#         leap_count += 1
#     else:
#         print(str(year) + " → No Event")
#     year += 1

# print()
# print("Total Leap Years =", leap_count)
# print("Total Events Scheduled =", leap_count)