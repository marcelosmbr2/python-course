# ============================================================
# WEB SCRAPING - PAGINATION (MULTIPLE PAGES)
# ============================================================
# Most sites split content across pages
# We need to loop through all of them to collect everything

import requests
from bs4 import BeautifulSoup
import time  # to pause between requests (good practice!)


# ============================================================
# 1. UNDERSTANDING PAGINATION
# ============================================================
# Common URL pagination patterns:
#
# Query parameter:
#   site.com/products?page=1
#   site.com/products?page=2
#
# URL segment:
#   site.com/catalog/page-1.html
#   site.com/catalog/page-2.html
#
# Strategy: find the pattern and iterate with a loop


# ============================================================
# 2. NUMERIC URL PAGINATION
# ============================================================

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# Collecting 3 pages as an example
for page_number in range(1, 4):  # pages 1, 2 and 3
    url = BASE_URL.format(page_number)
    print(f"Scraping page {page_number}...")

    response = requests.get(url)

    # Check if the page exists
    if response.status_code != 200:
        print(f"Page {page_number} not found. Stopping.")
        break

    # Parse the page and collect book data
    soup = BeautifulSoup(response.text, "html.parser")
    # Each book is in an <article class="product_pod"> element
    books = soup.select("article.product_pod")

    for book in books:
        title = book.select_one("h3 > a").get("title")
        price = book.select_one("p.price_color").get_text(strip=True)
        all_books.append({"title": title, "price": price})

    time.sleep(1)  # 1-second pause between pages (be kind to the server!)

print(f"\nTotal collected: {len(all_books)} books")


# ============================================================
# PAGINATION BEST PRACTICES
# ============================================================
# ✓ Always use time.sleep() between requests
# ✓ Check status_code before processing
# ✓ Follow the site's own "next" link (more robust than manual URLs)
# ✓ Set a maximum limit so the loop doesn't run forever
# ✓ Handle connection errors with try/except