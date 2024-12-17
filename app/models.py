from pydantic import BaseModel


class PriceData(BaseModel):
    currency_code: str
    currency_name: str
    exchange_rate: str
