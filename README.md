# webscrape-with-scrapy


# 🛒 Keells Supermarket Product Scraper (Scrapy + Selenium)

This Scrapy project scrapes product data from [Keells Supermarket](https://www.keellssuper.com/) using **Selenium** for JavaScript rendering and **BeautifulSoup** for parsing.

---

## ✅ Features

- Scrapes from all main categories:
  - Snacks
  - Fresh Fruits
  - Grocery
  - Bakery
  - Chilled Products
  - Household Essentials
  - Electronic Devices
- Uses **Selenium scrolling** to load all products
- Extracts:
  - Category
  - Product Name
  - Final Price
  - Original Price (if available)
  - Discount (if available)
  - Image URL
- Exports scraped data to CSV file (via Scrapy CLI)

---

## 📁 Project Structure

## 📂 Project Structure

```text
keells_scraper/
├── scrapy.cfg                       # Scrapy project configuration file
├── keells_scraper/                 # Main project module
│   ├── __init__.py
│   ├── items.py                    # Define item structures
│   ├── middlewares.py              # Custom middlewares (optional)
│   ├── pipelines.py                # Item pipelines (optional)
│   ├── settings.py                 # Project settings (configure feed/export here)
│   └── spiders/
│       └── all_keells_categories.py   # The spider that scrapes all categories
├── screenshots/                    # Screenshots folder used in README
│   ├── keells_home.png
│   ├── keells_category.png
│   └── keells_snacks_view.png
└── keells_all.csv                  # Final output CSV after spider run
```


## 🛠 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (matching your Chrome version)

Install dependencies:

```bash
pip install scrapy selenium beautifulsoup4
```

#Run and Save Output
bash

scrapy crawl quotes_spider -o keells_all.csv



