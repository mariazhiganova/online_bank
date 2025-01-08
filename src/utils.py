import json

import pandas as pd


def get_xlsx(file_path: str) -> list[dict]:
    """
    Функция, принимающая путь до Excel-файла и возвращающая список словарей.
    """
    try:

        df = pd.read_excel(file_path)
        if isinstance(df, pd.DataFrame) and not df.empty:
            return df.to_dict(orient="records")

        else:
            return []

    except FileNotFoundError:
        return []


def get_json_currencies(file_path: str) -> list:
    """
    Функция, принимающая путь к JSON файлу и возвращающая список данных из файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if "user_currencies" in data:
                result = data["user_currencies"]

        return result

    except json.JSONDecodeError as ex:
        raise ValueError(f"Ошибка при чтении файла: {ex}")

    except Exception as ex:
        raise Exception(f"Ошибка при чтении файла: {ex}")


def get_json_stocks(file_path: str) -> list:
    """
    Функция, принимающая путь к JSON файлу и возвращающая список данных из файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if "user_stocks" in data:
                result = data["user_stocks"]

            return result

    except json.JSONDecodeError as ex:
        raise ValueError(f"Ошибка при чтении файла: {ex}")

    except Exception as ex:
        raise Exception(f"Ошибка при чтении файла: {ex}")
