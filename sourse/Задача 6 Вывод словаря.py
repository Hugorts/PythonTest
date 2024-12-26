# На входе многомерный список, каждый элемент содержит информацию о товаре,
# количестве и цене, которые были в каком-то заказе. Например: [[Товар1, 1,500],

orders = [
    ["Товар1", 1, 500],
    ["Товар2", 7, 1000],
    ["Товар3", 6, 900],
    ["Товар4", 4, 129]
]

total_cost_item = {}

for item in orders:
    product, quantity, price = item
    total_cost = quantity * price

    if product in total_cost_item:
        total_cost_item[product] += total_cost
    else:
        total_cost_item[product] = total_cost

for product, total_cost in total_cost_item.items():
    print(f"{product}: {total_cost} рублей")

total_order_cost = sum(total_cost_item.values())
print(f"Общая стоимость всех товаров: {total_order_cost} рублей")

print(total_cost_item)