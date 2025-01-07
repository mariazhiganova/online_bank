import os
from datetime import datetime, timedelta
from typing import Dict, Union
import requests
from dotenv import load_dotenv

load_dotenv()
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")


def get_currency_rate(currency: str, amount: int = 1) -> Dict[str, Union[str, float]]:
    """
     Функция, принимающая на вход валюту для конвертации, сумму (по умолчанию 1) и возвращающая словарь в формате:
     {"currency": "валюта",
      "rate": стоимость в рублях}
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": CURRENCY_API_KEY}
    response = requests.get(url, headers=headers)
    status_code = response.status_code


    if status_code == 200:
        content = response.json()

        if content['result']:
            result = {'currency': currency, 'rate': round(content['result'], 2)}

            return result

        else:
            raise ValueError('Недостаточно данных')

    else:
        raise Exception(f'Запрос не был успешным. Возможная причина: {response.reason}')


def get_stock_price(stock: str) -> Dict[str, Union[str, float]]:
    """
    Функция, принимающая название акции и возвращающая словарь в формате:
    {"stock": "Название акции",
      "price": стоимость акции}
    """
    date_yesterday = datetime.now() - timedelta(days=1)
    three_days_ago = datetime.now() - timedelta(days=3)
    stop_date = date_yesterday.strftime("%Y-%m-%d")
    start_date = three_days_ago.strftime("%Y-%m-%d")
    headers = {"apikey": STOCK_API_KEY}
    url = f'https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/{start_date}/{stop_date}?apiKey={STOCK_API_KEY}'


    response = requests.get(url, headers=headers)

    status_code = response.status_code

    if status_code == 200:
        content = response.json()
        print(content)

        if content['results'][0]['c']:
            result = {"stock": stock, "price": content['results'][0]['c']}

            return result

    else:
        raise Exception(f'Запрос не был успешным. Возможная причина: {response.reason}')

if __name__ == '__main__':
    #print(get_currency_rate('USD'))
    print(get_stock_price('AAPL'))