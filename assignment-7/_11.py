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
    if travel_class == "sleeper":
        fare = 100
    else:
        fare = 200
elif distance <= 500:
    if travel_class=="sleeper":
        fare = 300
    else:
        fare = 600
else:
    if travel_class == "sleeper":
        fare = 500
    else:
        fare = 1000
print("Total Fare: ₹" + str(fare))