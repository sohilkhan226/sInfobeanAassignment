# Assignment 4: Travel Distance Calculation

# A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

# Input:
# Speed = 60 km/hr
# Time = 2 hours 30 minutes

# Expected Output:
# Total Time = 2.5 hours
# Distance = 150.0 km

speed = 60
hours = 2
minutes = 30

total_time = hours + minutes / 60
distance = speed * total_time

print("Total Time =", total_time, "hours")
print("Distance =", distance, "km")