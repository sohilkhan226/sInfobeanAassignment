# Note:

# * Do NOT use if-else
# * All percentages are given as whole numbers (like 5, 10). Convert using (value ÷ 100)
# * Follow correct operator precedence and associativity
# * Use ** for power (exponent), not ^

# Assignment 1: Restaurant Bill Split

# A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

# Input:
# Total bill amount = 2500
# GST = 5%
# Service charge = 10%
# Number of friends = 4

# Expected Output:
# Final Bill = 2875.0
# Each Person Pays = 718.75


bill = float(input("Enter total bill amount: "))
gst_rate = float(input("Enter GST rate: "))
service_rate = float(input("Enter service charge rate: "))
friends = int(input("Enter number of friends: "))

gst = bill * gst_rate / 100                    # 5% GST
service = bill * service_rate / 100            # 10% service
final_bill = bill + gst + service

each_person = final_bill / friends

print("Final Bill =", final_bill)
print("Each Person Pays =", each_person)