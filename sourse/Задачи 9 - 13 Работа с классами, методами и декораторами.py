# 9. Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения.
# 10. Создайте метод, который выводит ФИО.
# 11. Создайте метод, который вычисляет возраст в годах.
# 12. Создайте класс - наследник вашего первого класса. Перекройте в нём метод,
#     вычисляющий возраст в годах на метод, который вычисляет возраст в днях.
# 13. Создайте декоратор для метода, который выводит ФИО. Пусть новый метод
#     выводит ФИО, заключенное в теги <strong>.

from datetime import datetime

def strong_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}<strong>"

    return wrapper

class Person:
    def __init__(self, last_name, first_name, patronymic, birth_year):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birth_year = birth_year

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def calculate_age_in_years(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

# Класс-наследник с перекрытием метода
class BrandNewPerson(Person):
    def calculate_age_in_years(self):
        current_date = datetime.now()
        birth_date = datetime(self.birth_year, 1, 1)
        age_in_days = (current_date - birth_date).days
        return age_in_days

    @strong_decorator
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


person = Person("Иванов", "Иван", "Иванович",2002 )
BrandNew_person = BrandNewPerson("Петров", "Петр", "Андреевич",1985)


print("ФИО обычного человека:", person.get_full_name())
print("ФИО BrandNew человека:", BrandNew_person.get_full_name(), '\n')

print("Возраст в годах(Person Class):", person.calculate_age_in_years())
print("Возраст в днях(BrandNewPerson Class):", BrandNew_person.calculate_age_in_years())
