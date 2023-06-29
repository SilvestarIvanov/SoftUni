elements = input().split()

bakery_products = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    bakery_products[key] = value

print(bakery_products)