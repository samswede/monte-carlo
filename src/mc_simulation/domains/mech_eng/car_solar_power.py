# Constants and assumptions for the calculation
area = 1.5  # m² (assumed area of solar panels on a car roof)
efficiency = 0.20  # 20% efficient solar panels
sunlight_intensity = 6.0  # average kWh/m²/day in Phoenix
angle_of_incidence = 0  # Assuming a flat roof, 0 degrees from perpendicular

# Calculate the solar power in kWh
# Since angle of incidence is 0, cos(0) is 1, so it doesn't affect the calculation
solar_power = area * efficiency * sunlight_intensity

# Convert the solar power from kWh to W (since it's per day, divide by 24 to get kW)
solar_power_w = solar_power*1000 / 24  # converting kWh/day to W

print(f'solar_power Watts: {solar_power_w}')