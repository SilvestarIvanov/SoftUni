lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet_price = lost_fights_count // 2
trashed_sword_price = lost_fights_count // 3
trashed_shield_price = lost_fights_count // (2 * 3)
trashed_armor_price = trashed_shield_price // 2

total_expenses = trashed_helmet_price * helmet_price + trashed_sword_price * sword_price + trashed_shield_price * shield_price + trashed_armor_price * armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")