# Assignment 9: Fuel Cost Calculator

# Write a Python program that:

# Accepts distance (km), mileage (km/litre), and petrol price.
# Calculates total fuel cost.

# Input:
# Distance = 100
# Mileage = 20
# Petrol Price = 100

# Output:
# Cost = 500

distance = float(input("Enter distance in km: "))
mileage = float(input("Enter mileage in km/litre: "))
petrol_price = float(input("Enter petrol price per litre: "))

cost = (distance / mileage) * petrol_price

print("Cost =", cost)