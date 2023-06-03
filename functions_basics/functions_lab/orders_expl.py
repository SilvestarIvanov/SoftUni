product = input()
price = int(input())
coffee = 1.50
water = 1
coke = 1.40
snacks = 2
sum_price=0
def order_price(operator: str, price_order: int):
    if operator == "coffee":
        return f"{price_order * coffee:.2f}"
    elif operator == "coke":
        return f"{price_order * coke:.2f}"
    elif operator == "water":
        return f"{price_order * water:.2f}"
    elif operator == "snacks":
        return f"{price_order * snacks:.2f}"

print(order_price(product, price))