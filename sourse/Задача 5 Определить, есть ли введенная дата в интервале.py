#  Пользователь вводит две даты в формате ДД.ММ.ГГГГ  ЧЧ:ММ. Пользователь вводит третью дату в формате  ДД.ММ.ГГГГ  ЧЧ:ММ.
#  Определить, лежит ли дата внутри временного интервала, образованного первыми двумя датами.
from datetime import datetime

def check_time(date_time_1, date_time_2, date_time_3):
    time_difference = date_time_2 - date_time_1
    interval = time_difference.total_seconds()
    if interval > 0:
        check = date_time_1 - date_time_3
        if check.total_seconds() < 0 and abs(check.total_seconds()) > interval:
            return print("Введенная вами дата позже чем конец интервала!")
        elif check.total_seconds() < 0 and abs(check.total_seconds()) < interval:
            return print("Введенная вами дата входит в указанный интервал!")
        else:
            print("Введенная вами дата раньше чем начало интервала!")
    elif interval < 0:
        check = date_time_2 - date_time_3
        if check.total_seconds() < 0 and abs(check.total_seconds()) > abs(interval):
            return print("Введенная вами дата позже чем конец интервала!")
        elif check.total_seconds() < 0 and abs(check.total_seconds()) < abs(interval):
            return print("Введенная вами дата входит в указанный интервал!")
        else:
            print("Введенная вами дата раньше чем начало интервала!")
    else:
        print("Минимальный интервал минута!")

# Суть в том, что сначала я нахожу нижнюю границу интервала, за счет вычитания одной границы из другой. Далее я считаю величину в секундах между границами.
# Проверяю с помощью нижней границы введенную дату. Если величина в секундах отрицательна, что говорит о том, что введеная дата
# больше нижней границы и при этом абсолютное значение величины больше интервала в секундах, то дата больше верхней границы.

# Если же число также отрицательно, но меньше величины между границами, то значит оно внутри интервала.
# В остальных случаях число меньше нижней границы.
from datetime import datetime

user_input_1 = input("Введите первую дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: ")
user_input_2 = input("Введите вторую дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: ")
user_input_3 = input("Введите для проверки дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ: ")

date_time_1 = datetime.strptime(user_input_1, "%d.%m.%Y %H:%M")
date_time_2 = datetime.strptime(user_input_2, "%d.%m.%Y %H:%M")
date_time_3 = datetime.strptime(user_input_3, "%d.%m.%Y %H:%M")

check_time(date_time_1, date_time_2, date_time_3)

