#Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000
summ_even = 0
summ_odd = 0
for digit in range(100,1001):
    if digit % 2 != 0:
        summ_odd+=digit
    else:
        summ_even+=digit
print(f'Сумма четных чисел: {summ_even}', '\n' f'Сумма нечетных чисел: {summ_odd}')