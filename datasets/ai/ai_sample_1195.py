import numpy as np

# Calculate the soil moisture
def calculate_soil_moisture(temperature, humidity, soil_type):
    # Calculation for sandy soil
    moisture = 0
    if soil_type == "sandy":
        moisture = (temperature - 10) * humidity * 0.5
    # Calculation for loamy soil
    elif soil_type == "loamy":
        moisture = (temperature - 20) * humidity * 0.6
    # Calculation for clay soil
    elif soil_type == "clay":
        moisture = (temperature - 30) * humidity * 0.8
    # Other types
    else:
        moisture = 10
    # Calculate irrigation amount
    if moisture > 4:
        # No irrigation needed
        irrigation_amount = 0
    else:
        # Irrigate the land
        irrigation_amount = np.abs(4 - moisture)
    return irrigation_amount