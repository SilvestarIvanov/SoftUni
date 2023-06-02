product = input()
price = int(input())
coffee = 1.50
water = 1
coke = 1.40
snacks = 2
def order_price(operator: str, price_order: int):
    if operator == "coffee":
        print(f"{price_order * coffee:.2f}")
    elif operator == "coke":
        print(f"{price_order * coke:.2f}")
    elif operator == "water":
        print(f"{price_order * water:.2f}")
    elif operator == "snacks":
        print(f"{price_order * snacks:.2f}")

order_price(product, price)