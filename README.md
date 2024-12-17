# Exchange Rate Scraper

This project scrapes exchange rates from the Central Bank of Iran's website (cbi.ir) and serves the data through a FastAPI endpoint.

# Installation

1. Clone the git repository

```
git clone https://github.com/devmmk/cbi-scraper.git
cd cbi-scraper
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. Access the data at http://127.0.0.1:8000/prices

## Features

- Scrapes exchange rates every 60 seconds.
- Exposes an API to get the latest exchange rates.