# 2.
# Digit Threshold Break Analyzer

# A monitoring system analyzes numeric IDs to detect high-value digits. 
# The system keeps adding digits one by one, but stops processing as soon as the running sum exceeds a given threshold.

# Write a program to:

# Accept a number and a threshold value
# Traverse digits from right to left
# Keep adding digits to a running sum
# Display each digit added
# The moment sum exceeds the threshold, stop using break
# Display:
# - Digits processed
# - Final sum
# - Count of digits processed
# If threshold is never exceeded, print Threshold Not Reached

# Use loops and break wherever required.

# Input:
# 57294
# Threshold = 10

# Output:
# Digits Processed: 4 9
# Sum = 13
# Count = 2
# Threshold Exceeded

# Input:
# 1234
# Threshold = 15

# Output:
# Digits Processed: 4 3 2 1
# Sum = 10
# Count = 4
# Threshold Not Reached

num_str = input()
threshold_input = input()

# Robust parsing to handle both "10" and "Threshold = 10" formats
threshold = int(threshold_input.split('=')[-1].strip())

running_sum = 0
count = 0
processed = []
exceeded = False

# Traverse from right to left
i = len(num_str) - 1
while i >= 0:
    d = int(num_str[i])
    running_sum += d
    processed.append(d)
    count += 1
    
    # Stop immediately if threshold is exceeded
    if running_sum > threshold:
        exceeded = True
        break
    i -= 1

# Display results
print("Digits Processed:", end=" ")
for p in processed:
    print(p, end=" ")
print()
print("Sum =", running_sum)
print("Count =", count)

if exceeded:
    print("Threshold Exceeded")
else:
    print("Threshold Not Reached")