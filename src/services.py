import json
from datetime import datetime


def get_profitable_cashback_categories(data: list, year: str, month: str) -> str:
    """
    На вход функции поступают данные для анализа, год и месяц.
    На выходе — JSON с анализом, сколько на каждой категории можно заработать кешбэка в указанном месяце года,
    в формате:
    {"Категория 1": 1000,
    "Категория 2": 2000,
    "Категория 3": 500}
    """
    filtered_data = []
    result = {}

    if data:
        for x in data:
            date_obj = datetime.strptime(x['Дата операции'], '%d.%m.%Y %H:%M:%S')
            year_part = date_obj.strftime('%Y')
            month_part = date_obj.strftime('%m')

            if year_part == year and month_part == month:
                filtered_data.append(x)
                category = x['Категория']
                amount = x['Сумма операции']

                if category not in result and amount < 0:
                    if category != 'Переводы':
                        result[category] = 0.0

                        result[category] += abs(amount * 0.01)

    filtered_result = dict(sorted(result.items(), key=lambda value: value[1], reverse=True))
    parsed_result = json.dumps(filtered_result, ensure_ascii=False)

    return parsed_result
