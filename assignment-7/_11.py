# 11. Railway Ticket Fare System


# A railway system calculates ticket fare based on distance and travel class:

# * Distance ≤100 km:
#   Sleeper → ₹100, AC → ₹200
# * Distance 101–500 km:
#   Sleeper → ₹300, AC → ₹600
# * Distance >500 km:
#   Sleeper → ₹500, AC → ₹1000

# Write a Python program to calculate ticket fare.

# Input:
# Enter distance: 350
# Enter class: AC

# Output:
# Total Fare: ₹600

distance = int(input("Enter distance: "))
travel_class = input("Enter class: ").strip()

if distance <= 100:
    if travel_class == "Sleeper":
        fare = 100
    elif travel_class == "AC":
        fare = 200
elif distance <= 500:
    if travel_class == "Sleeper":
        fare = 300
    elif travel_class == "AC":
        fare = 600
else:
    if travel_class == "Sleeper":
        fare = 500
    elif travel_class == "AC":
        fare = 1000

print("Total Fare: ₹" + str(fare))