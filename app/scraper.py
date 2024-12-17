import json
import time
import os
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from app.models import PriceData


class Scraper:
    def __init__(self, url, file_path, interval=60):
        self.url = url
        self.file_path = file_path
        self.interval = interval
        self.thread = threading.Thread(target=self.scrape_data, daemon=True)

    def start(self):
        self.thread.start()

    def scrape_data(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        while True:
            try:
                driver.get(self.url)
                time.sleep(5)

                prices_data = []
                rows = driver.find_elements(By.XPATH, "//tbody//tr")

                for row in rows:
                    columns = row.find_elements(By.TAG_NAME, "td")
                    if len(columns) == 6:
                        price_data = PriceData(
                            currency_code=columns[0].text.strip(),
                            currency_name=columns[1].text.strip(),
                            exchange_rate=columns[2].text.strip(),
                        )
                        prices_data.append(price_data)

                with open(self.file_path, 'w', encoding='utf-8') as f:
                    json.dump([data.dict() for data in prices_data], f, ensure_ascii=False, indent=4)

            except (TimeoutException, NoSuchElementException) as e:
                print(f"Error: {e}. Retrying in {self.interval} seconds.")
            except Exception as e:
                print(f"Unexpected error: {e}. Retrying in {self.interval} seconds.")
            
            time.sleep(self.interval)
        driver.quit()
