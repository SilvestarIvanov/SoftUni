import re

command = input()
furniture_bought = []
total_money = 0
pattern = r">>([A-Za-z]+)<<(\d+.?\d*)!(\d+)"


while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        furniture_bought.append(furniture)
        total_money += float(price) * int(quantity)

    command = input()
print("Bought furniture:")
for furniture in furniture_bought:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")