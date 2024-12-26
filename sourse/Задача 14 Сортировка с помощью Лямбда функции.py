
# Отсортируйте список из задачи 6 по: товару, по сумме в строке (количество*цену).
# Используйте для сортировки лямда функцию.

orders = [
    ["Товар1", 1, 500],
    ["Товар2", 7, 1000],
    ["Товар3", 6, 900],
    ["Товар3", 6, 200],
    ["Товар4", 2, 920],
    ["Товар5", 4, 405],
    ["Товар6", 7, 130],
    ["Товар7", 8, 930],
    ["Товар8", 1, 200]
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

sorted_by_product = sorted(orders, key=lambda x: x[0])
print("Сортировка по товару:")
for item in sorted_by_product:
    print(item)

sorted_by_total_cost = sorted(orders, key=lambda x: x[1] * x[2], reverse=True)
print("\nСортировка по общей стоимости заказа (количество * цена):")
for item in sorted_by_total_cost:
    print(item)