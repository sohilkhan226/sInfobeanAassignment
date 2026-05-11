# 12. Restaurant Bill with GST System

# A restaurant applies GST based on the total bill amount:

# * Up to ₹1000 → 5% GST
# * ₹1001 to ₹5000 → 12% GST
# * Above ₹5000 → 18% GST
#   Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

# Write a Python program to calculate the final bill.

# Input:
# Enter bill amount: 4000

# Output:
# Final Bill Amount: ₹4680

bill = float(input("Enter bill amount: "))

if bill <= 1000:
    gst = bill * 5 / 100
elif bill <= 5000:
    gst = bill * 12 / 100
else:
    gst = bill * 18 / 100

if bill > 3000:
    service_charge = 200
else:
    service_charge = 0

final_bill = bill + gst + service_charge

print("Final Bill Amount: ₹" + str(int(final_bill)))