import logging
from datetime import datetime
from typing import Optional

import pandas as pd

from src.decorators import decorator_record_file
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("my_log")


@decorator_record_file("reports.json")
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    Функция принимает на вход датафрейм с транзакциями, название категории, и опциональную дату в формате ДД.ММ.ГГГГ.
    Если дата не передана, то берется текущая дата.
    И возвращает траты по заданной категории за последние три месяца (от переданной даты).
    """
    if not date:
        stop_date = datetime.now()

    else:
        stop_date = datetime.strptime(date, "%d.%m.%Y")

    logger.info('Определение даты, начиная с которой будут взяты операции для подсчета трат по категориям')

    start_date = stop_date - pd.Timedelta(days=90)

    logger.info('Преобразование дат операций в объект datatime')

    transactions["Дата платежа"] = pd.to_datetime(transactions["Дата платежа"], format="%d.%m.%Y")

    logger.info('Формирование списка операций для формирвоания отчета')

    filtered_transactions = transactions[
        (transactions["Дата платежа"] >= start_date)
        & (transactions["Дата платежа"] <= stop_date)
        & (transactions["Категория"] == category)
        & (transactions["Сумма операции"] < 0)
    ]

    logger.info('Инициализация отчета')

    result = filtered_transactions.groupby("Категория")["Сумма операции"].apply(lambda x: x.abs().sum()).reset_index()

    return result
