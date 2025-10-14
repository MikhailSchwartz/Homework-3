import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_rub(amount: float, currency: str) -> float | str:
    """
    Конвертирует сумму в указанной валюте в рубли, используя Exchange Rates Data API.
    """
    api_key = os.getenv("API_KEY")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Ошибка API {response.status_code}"
        data = response.json()

        if data.get("success"):
            return float(data.get("result"))
        else:
            return "Ошибка обработки запроса конвертации"

    except requests.exceptions.RequestException as e:
        return f"Ошибка HTTP: {type(e)}"


# if __name__ == "__main__":
#     print(convert_rub(100.0, "USD"))
