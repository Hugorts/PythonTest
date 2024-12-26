#Пользователь вводит дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ. Обрежьте секунды. Замените час на 10.
from datetime import datetime, timedelta

user_input = input("Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: ")

date_time = datetime.strptime(user_input, "%d.%m.%Y %H:%M")
updated_date_time = date_time.replace(hour=10)

print(f' Преобразованная дата {updated_date_time.strftime("%d.%m.%Y %H:%M")}')
