number_of_lines = int(input())

water_tank = 255
capacity = 0
for i in range(number_of_lines):
    liters_of_water = int(input())
    capacity += liters_of_water
    if capacity > water_tank:
        capacity -= liters_of_water
        print(f"Insufficient capacity!")
        continue

print(capacity)
