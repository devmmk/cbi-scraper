import json
import os
from app.models import PriceData

prices_file = "prices.json"


def read_prices():
    if os.path.exists(prices_file):
        with open(prices_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [PriceData(**item) for item in data]
    return None
