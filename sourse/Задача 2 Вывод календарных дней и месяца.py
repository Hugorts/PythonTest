#Пользователь вводит дату в формате ДД.ММ.ГГГГ. Вывести первый день месяца, последний день месяца, сам месяц.

from datetime import datetime, timedelta

def process_date(input_date):
    date = datetime.strptime(input_date, "%d.%m.%Y")
    first_day = date.replace(day=1)
    next_month = date.replace(day=28) + timedelta(days=4) # Прибавляю + 4 дня, чтобы гарантированно перейти на следующий месяц,
    last_day = next_month.replace(day=1) - timedelta(days=1) # затем отнимаю один день, чтобы перейти на последнее число исходного месяца
    month_name = date.strftime("%B")

    return first_day, last_day, month_name


user_input = input("Введите дату в формате ДД.ММ.ГГГГ: ")
result = process_date(user_input)

first_day, last_day, month_name = result
print(f"Первый день месяца: {first_day.strftime('%d.%m.%Y')}")
print(f"Последний день месяца: {last_day.strftime('%d.%m.%Y')}")
print(f"Месяц: {month_name}")
