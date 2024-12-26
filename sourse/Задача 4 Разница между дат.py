# Пользователь вводит две даты в формате ДД.ММ.ГГГГ  ЧЧ:ММ. Вывести разницу между датами в часах, днях (целых), минутах и секундах.

from datetime import datetime

user_input_1 = input("Введите первую дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: ")
user_input_2 = input("Введите вторую дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: ")

date_time_1 = datetime.strptime(user_input_1, "%d.%m.%Y %H:%M")
date_time_2 = datetime.strptime(user_input_2, "%d.%m.%Y %H:%M")

time_difference = abs(date_time_2 - date_time_1)
seconds = int(time_difference.total_seconds())
minutes = int(seconds // 60)
hours = int(minutes // 60)
days = int(hours // 24)

print(f"Разница между введенными датами в разных единицах: \n дни: {days} \n часы: {hours} \n минуты: {minutes} \n секунды: {seconds}")
