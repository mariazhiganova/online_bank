import re
from datetime import datetime, time, timedelta
from typing import List


def greetings(actual_time: str) -> str:
    """
    Функция, принимающая время в виде строки в формате HH:MM:SS
    и возвращающая приветствие в зависимости от времени суток.
    """
    try:
        date_obj = datetime.strptime(actual_time, '%H:%M:%S')

        greets = ['Доброе утро!', 'Добрый день!', 'Добрый вечер!', 'Доброй ночи!']

        comparison_night = time(0, 0)
        comparison_morning = time(4, 0)
        comparison_day = time(12, 0)
        comparison_evening = time(17, 0)

        if comparison_night <= date_obj.time() < comparison_morning:
            greet = greets[3]

        elif comparison_morning <= date_obj.time() < comparison_day:
            greet = greets[0]

        elif comparison_day <= date_obj.time() < comparison_evening:
            greet = greets[1]

        else:
            greet = greets[2]

        return greet

    except ValueError:
        raise ValueError('Неверный формат времени')


def sort_by_date(operations_list: list[dict], input_date: str) -> str | list[dict]:
    """
    Функция, получающая список словарей с операциями и дату, возвращающая список, отфильтрованный
    по дате с начала месяца, на который выпадает входящая дата, по входящую дату.
    """
    pattern = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')

    result = []

    if input_date and pattern.fullmatch(input_date):
        day_int = int(input_date[:2])
        input_date_obj = datetime.strptime(input_date, '%d.%m.%Y').date()

        start = input_date_obj - timedelta(days=(day_int - 1))
        stop = input_date_obj

        for operation in operations_list:
            operation_date_obj = datetime.strptime(operation['Дата операции'], '%d.%m.%Y %H:%M:%S').date()
            if start <= operation_date_obj <= stop:
                result.append(operation)

    else:
        print('Введена неверная дата. Введите дату в формате ДД.ММ.ГГГГ')

    return result


def get_card_info(operations_list: list[dict]) -> list[dict]:
    """
    Функция, принимающая список операций и возвращающая список словарей с данными о картах:
    последние 4 цифры карты, общая сумма расходов, кешбэк (1 рубль на каждые 100 рублей) в формате
    [{"last_digits": "4 последние цифры номера карты",
      "total_spent": сумма расходов,
      "cashback": кэшбек},
    {...}]
    """
    card_data = {}
    pattern = re.compile(r'\*\d{4}')

    for operation in operations_list:

        if isinstance(operation['Номер карты'], str) and pattern.fullmatch(operation['Номер карты']):
            if 'Сумма операции' in operation and 'Статус' in operation:

                card_number = operation['Номер карты'][1:]
                amount = operation['Сумма операции']

                if operation['Статус'] == "OK" and float(amount) < 0:
                    if card_number not in card_data:
                        card_data[card_number] = 0.0
                    card_data[card_number] += abs(float(amount))

    result = []
    for card_num, data in card_data.items():
        last_digits = card_num
        total_spent = data
        cashback = total_spent * 0.01

        result.append({
            'last_digits': last_digits,
            'total_spent': round(total_spent, 2),
            'cashback': round(cashback, 2)
        })

    return result


def get_top_transactions(operations_list: list[dict]) -> list[dict]:
    """
    Функция, принимающая список словарей с операциями и возвращающая список из топ-5 транзакций по сумме
    в формате:
    [{"date": "дата",
      "amount": сумма,
      "category": "категория",
      "description": "описание"},
    {...}]
    """
    n = 5
    result = []

    negative_transactions = [operation for operation in operations_list if
                             'Сумма операции' in operation and operation['Сумма операции'] < 0]

    top_5 = sorted(negative_transactions, key=lambda x: abs(x['Сумма операции']), reverse=True)[:n]

    for el in top_5:
        date = el['Дата операции'].split()[0]
        amount = abs(el['Сумма операции'])
        category = el['Категория']
        description = el['Описание']

        short_info = {
            'date': date,
            'amount': round(amount, 2),
            'category': category,
            'description': description
        }
        result.append(short_info)

    return result
