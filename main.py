import json
from datetime import datetime

from settings import EXCEL_PATH, JSON_PATH
from src.views import greetings, sort_by_date, get_card_info, get_top_transactions
from src.utils import get_xlsx, get_json_stocks, get_json_currencies
from src.external_api import get_currency_rate, get_stock_price


def views_main(date: str) -> str:
    """
    Функция, принимающая на вход строку с датой и временем
    в формате YYYY-MM-DD HH:MM:SS и возвращающая JSON-ответ
    """

    actual_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    correct_date = actual_date.strftime('%d.%m.%Y')
    correct_time = actual_date.strftime('%H:%M:%S')

    operations_list = get_xlsx(EXCEL_PATH)
    sort_operations_list = sort_by_date(operations_list, correct_date)

    greeting = greetings(correct_time)
    cards = get_card_info(sort_operations_list)
    top_transactions = get_top_transactions(sort_operations_list)
    currency_rates = [get_currency_rate(cur) for cur in get_json_currencies(JSON_PATH)]
    stock_prices = [get_stock_price(st) for st in get_json_stocks(JSON_PATH)]

    result = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }

    parsed_result = json.dumps(result, ensure_ascii=False)

    return parsed_result


if __name__ == "__main__":
    my_date = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
    print(views_main(my_date))
