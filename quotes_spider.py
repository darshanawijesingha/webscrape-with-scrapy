import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.parse import urlparse

class AllKeellsSpider(scrapy.Spider):
    name = "quotes_spider"

    # ✅ Add all category URLs here
    start_urls = [
        "https://www.keellssuper.com/snacks",
        "https://www.keellssuper.com/fresh-fruits",
        "https://www.keellssuper.com/grocery",
        "https://www.keellssuper.com/keells-bakery",
        "https://www.keellssuper.com/chilled-products",
        "https://www.keellssuper.com/household-essentials",
        "https://www.keellssuper.com/electronic-devices"
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(3)

        # Scroll to load all items
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Get HTML
        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        # Extract category name from URL (e.g., "snacks" from ".../snacks")
        category = urlparse(response.url).path.strip("/").replace("-", "_")

        products = soup.find_all("div", class_="product-card-container")

        for product in products:
            name_tag = product.find("div", class_="product-card-name btn col-md-12")
            final_price_tag = product.find("div", class_="product-card-final-price")
            original_price_tag = product.find("div", class_="product-card-original-price")
            discount_tag = product.find("div", class_="product-card-promotion-badge-percentage")
            image_tag = product.find("img", class_="img-fluid")

            name = name_tag.get_text(strip=True) if name_tag else ""
            final_price = final_price_tag.get_text(strip=True) if final_price_tag else ""
            original_price = original_price_tag.get_text(strip=True) if original_price_tag else ""
            discount = discount_tag.get_text(strip=True) + "%" if discount_tag else ""
            image_url = image_tag['src'] if image_tag and "http" in image_tag['src'] else "https://www.keellssuper.com" + image_tag['src'] if image_tag else ""

            yield {
                "Category": category,
                "Product Name": name,
                "Final Price": final_price,
                "Original Price": original_price,
                "Discount": discount,
                "Image URL": image_url
            }

    def closed(self, reason):
        self.driver.quit()
