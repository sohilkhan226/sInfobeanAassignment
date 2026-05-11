# Assignment 10: Time Conversion

# Convert total seconds into hours, minutes, and seconds.

# Input:
# Total seconds = 7384

# Expected Output:
# Hours = 2
# Minutes = 3
# Seconds = 4

total_seconds = 7384

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)