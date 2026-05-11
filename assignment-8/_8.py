# 8. Smart Farming Irrigation System

# A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

# If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

# Input:
# Soil Moisture = 25
# Temperature = 36
# Crop = wheat

# Output:
# Irrigation = High Water Supply

soil_moisture = int(input("Enter soil moisture: "))
temperature = int(input("Enter temperature: "))
crop = input("Enter crop type: ").lower()

if soil_moisture <= 30:
    if temperature >= 35:
        if crop == "wheat":
            irrigation = "High Water Supply"
        else:
            irrigation = "Moderate Supply"
    else:
        irrigation = "Moderate Supply"
else:
    if soil_moisture <= 60:
        rainfall = input("Enter rainfall prediction (yes/no): ").lower()
        if rainfall == "yes":
            irrigation = "Delay Irrigation"
        else:
            irrigation = "Light Irrigation"
    else:
        irrigation = "No Irrigation"

print("Irrigation =", irrigation)