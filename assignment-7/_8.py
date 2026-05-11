# 8. Weather Monitoring System

# A weather monitoring system classifies the weather condition based on temperature:

# * Below 0°C → Freezing
# * 0°C to 20°C → Cold
# * 21°C to 35°C → Warm
# * Above 35°C → Hot

# Write a Python program to classify the weather.

# Input:
# Enter temperature: 38

# Output:
# Weather Condition: Hot

temperature = float(input("Enter temperature: "))

if temperature < 0:
    condition = "Freezing"
elif temperature <= 20:
    condition = "Cold"
elif temperature <= 35:
    condition = "Warm"
else:
    condition = "Hot"

print("Weather Condition:", condition)