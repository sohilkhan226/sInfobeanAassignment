# Assignment 6: Data Storage Conversion

# A user wants to convert data from GB into MB and KB.

# Input:
# Data = 5 GB

# Expected Output:
# In MB = 5120.0
# In KB = 5242880.0


data_gb = 5

data_mb = data_gb * 1024
data_kb = data_mb * 1024

print("In MB =", float(data_mb))
print("In KB =", float(data_kb))