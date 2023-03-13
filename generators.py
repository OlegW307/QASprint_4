import random
from datetime import date, timedelta


# Генератор человекообразных имен (согласная + гласная)
def generate_name():
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"
    name_len = random.randint(5, 10)
    name = random.choice(consonants).upper()
    for i in range(name_len - 1):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name


# Генератор адреса (строка)
def generate_adress():
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    index = ''.join([random.choice('0123456789') for _ in range(6)])
    street_name = ''.join([random.choice(alphabet) for _ in range(9)])
    street_name = street_name.capitalize() + random.choice(alphabet)
    house_number = random.randint(1, 200)
    flat_number = random.randint(1, 500)
    address = f"{index}, ул. {street_name}, д. {house_number}, кв. {flat_number}"
    return address


# Генератор телефонного номера
def generate_phone_number():
    prefix = "+"
    for i in range(10):
        prefix += str(random.randint(0, 9))
    return prefix


# генератор рандомной даты на год вперед
def date_to_order():
    today = date.today()
    days_to_add = random.randint(1, 365)
    new_date = today + timedelta(days=days_to_add)
    formatted_date = new_date.strftime('%d.%m.%Y')
    return formatted_date


# набор проверок корректности работы генераторов
print(f'Челоекообразное имя для заказа:', generate_name())
print(f'Адрес заказа:', generate_adress())
print(f'Телефон заказа:', generate_phone_number())
print(f'Дата заказа:', date_to_order())

