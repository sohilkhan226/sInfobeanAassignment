# 10.
# Electricity Bill Processing System (Multi-House)

# An electricity board processes bills for multiple houses in a society.

# Write a program to:

# - Read number of houses n
# - For each house:
#     - Read units consumed
#     - Calculate bill using slab rates:

#         First 100 units      → ₹5 per unit  
#         Next 100 units      → ₹7 per unit  
#         Above 200 units     → ₹10 per unit  

#     - Apply conditions:
#         - If bill > ₹2000 → add 10% surcharge  
#         - If units < 50 → give ₹100 subsidy  

#     - Print bill for each house

# - After processing all houses:
#     - Print total bill collected
#     - Print highest bill

# ---

# Input:
# 3
# 120
# 250
# 40

# Output:
# House 1 Bill = 640
# House 2 Bill = 1700
# House 3 Bill = 100

# Total Collection = 2440
# Highest Bill = 1700

n = int(input())

total_collection = 0
highest_bill = 0

for i in range(1, n + 1):
    units = int(input())
    
    # Slab calculation
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 500 + (units - 100) * 7
    else:
        bill = 1200 + (units - 200) * 10
        
    # Surcharge & Subsidy
    if bill > 2000:
        bill += bill * 0.10
    if units < 50:
        bill -= 100
        
    bill = int(bill)  # Clean integer output
    print(f"House {i} Bill = {bill}")
    
    total_collection += bill
    if bill > highest_bill:
        highest_bill = bill

print(f"\nTotal Collection = {int(total_collection)}")
print(f"Highest Bill = {highest_bill}")



#

# n = int(input())

# total_collection = 0
# highest_bill = 0
# i = 1

# while i <= n:
#     units = int(input())

#     # Slab calculation
#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = 500 + (units - 100) * 7
#     else:
#         bill = 1200 + (units - 200) * 10

#     # Surcharge & Subsidy
#     if bill > 2000:
#         bill += bill * 0.10
#     if units < 50:
#         bill -= 100

#     bill = int(bill)
#     print("House", i, "Bill =", bill)

#     total_collection += bill
#     if bill > highest_bill:
#         highest_bill = bill

#     i += 1

# print()
# print("Total Collection =", int(total_collection))
# print("Highest Bill =", highest_bill)