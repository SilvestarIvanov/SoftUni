days_of_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water = days_of_adventure * count_of_players * water_per_day_per_person
total_food = days_of_adventure * count_of_players * food_per_day_per_person

for num in range(1, days_of_adventure + 1):
    energy_lost = float(input())
    group_energy -= energy_lost
    if group_energy > 0:
        if num % 2 == 0:
            group_energy += group_energy * 0.05
            total_water = total_water - (total_water * 0.30)
        if num % 3 == 0:
            total_food -= total_food / count_of_players
            group_energy += group_energy * 0.10

if group_energy <= 0:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
