elements = input().split()

products = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    products[key] = value

searched_product = input().split()
for element in searched_product:
    if element in products:
        print(f"We have {products[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
