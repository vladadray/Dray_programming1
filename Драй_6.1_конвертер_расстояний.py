print("Введите расстояние в метрах:")
distance_m = float(input())

distance_km = distance_m / 1000
distance_ft = distance_m * 3.281
distance_inches = distance_m * 39.37
distance_yard = distance_m * 1.094
distance_miles = distance_m / 1609

print("Расстояние в километрах: ", distance_km)
print("Расстояние в футах: ", distance_ft)
print("Расстояние в дюймах: ", distance_inches)
print("Расстояние в ярдах: ", distance_yard)
print("Расстояние в милях: ", distance_miles)