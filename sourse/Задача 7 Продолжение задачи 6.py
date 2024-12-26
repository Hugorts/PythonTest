# Из задачи 6 постройте два списка идентификаторов товаров так, чтобы в каждом не было повторений

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


print("Словарь с общей суммой заказа:")
print(total_cost_item)

products = list(total_cost_item.items())

odd_group = products[::2] # берем например все нечетные идентификаторы - 1 список
even_group = products[1::2] # а тут возьмем все четные (массив с 0 начинается, значит отсчет с 1)

print("\n Список 1 идентификаторов товаров:")
print(even_group)

print("\n Список 2 идентификаторов товаров:")
print(odd_group)
