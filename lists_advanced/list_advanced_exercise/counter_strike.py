energy = int(input())
won_battles_count = 0
distance_real = 0
while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {won_battles_count}. Energy left: {energy}")
        break
    distance_real = int(distance)
    if energy >= distance_real:
        energy -= distance_real
        won_battles_count += 1
    else:
        print(f"Not enough energy! Game ends with {won_battles_count} won battles and {energy} energy")
        break
    if won_battles_count % 3 == 0:
        energy += won_battles_count
