# Assignment 1: Speed Calculator

# Write a Python program that:

# Accepts distance (in km) and time (in hours).
# Calculates speed.

# Input:
# Distance = 120
# Time = 2

# Output:
# # Speed = 60 km/h

distance = float(input("Enter distance in km: "))
time = float(input("Enter time in hours: "))

speed  =  distance / time     

print("Speed =", speed, "km/h")