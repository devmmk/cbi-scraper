from fastapi import FastAPI
from app.scraper import Scraper
from app.services import read_prices

app = FastAPI()

prices_file = "prices.json"
scraper = Scraper(url="https://www.cbi.ir/exrates/rates_fa.aspx", file_path=prices_file)
scraper.start()


@app.get("/prices")
async def get_prices():
    prices = read_prices()
    if prices is None:
        return {"error": "Prices data not available yet."}
    return prices


@app.get("/")
async def root():
    return {"message": "Exchange rate scraper is running."}
