# Assignment 9: Petrol Cost Calculation

# You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

# Input:
# Distance = 450 km
# Mileage = 15 km/litre
# Petrol price = 110/litre

# Expected Output:
# Petrol Used = 30.0 litres
# Total Cost = 3300.0

distance = 450
mileage = 15
petrol_price = 110

petrol_used = distance / mileage
total_cost = petrol_used * petrol_price

print("Petrol Used =", petrol_used, "litres")
print("Total Cost =", total_cost)