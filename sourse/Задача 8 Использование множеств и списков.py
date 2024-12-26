#  Из задачи 7 доработайте списки так, чтобы в каждом из двух списков были
#  элементы из другого. Переведите списки в множества. Возьмите объединение и
#  пересечение.

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

products = list(total_cost_item.keys())
print(products)
odd_group = products[::2]
even_group = products[1::2]

print("\n Список 1 идентификаторов товаров:")
print(even_group)

print("\n Список 2 идентификаторов товаров:")
print(odd_group)

for i in range(3):
    even_group.append(odd_group[i])
    odd_group.append(even_group[i])

print(f"\n Частично-объединенные списки: \n Список 1: {even_group} \n Список 2: {odd_group}") # Взял по 3 элемента из каждого списка и добавил в соседний

set_even_group = set(even_group)
set_odd_group = set(odd_group)

print(f"\n Списки, преобразованные в множества: \n Множество 1: {set_even_group} \n Множество 2: {set_odd_group}")

union_set = set_even_group.union(set_odd_group)
intersection_set = set_even_group.intersection(set_odd_group)
print("\nОбъединение множеств товаров:", union_set)
print("Пересечение множеств товаров:", intersection_set)