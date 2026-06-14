# ============================================================
# WEB SCRAPING - SAVING THE DATA
# ============================================================
# Collecting data is useless if we don't save it!
# Most common formats: CSV and JSON

import requests
from bs4 import BeautifulSoup
import csv
import json
import time


# ============================================================
# COLLECTING THE DATA (base for the examples below)
# ============================================================

def collect_books(num_pages=2):
    """Collects books from N pages of books.toscrape.com"""
    books = []

    for page in range(1, num_pages + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.select_one("h3 > a").get("title")
            price = book.select_one("p.price_color").get_text(strip=True)
            stars = book.select_one("p.star-rating").get("class")[1]
            available = "Yes" if book.select_one("p.instock") else "No"

            books.append({
                "title": title,
                "price": price,
                "stars": stars,
                "available": available
            })

        time.sleep(1)
        print(f"Page {page} done ({len(books)} books so far)")

    return books


books = collect_books(num_pages=2)
print(f"\nTotal: {len(books)} books collected\n")

# ============================================================
# 1. SAVING TO JSON
# ============================================================
# JSON is great for structured data, it is, easy to read and reuse

json_filename = "books.json"

with open(json_filename, "w", encoding="utf-8") as file:
    json.dump(books, file, ensure_ascii=False, indent=4)
    # ensure_ascii=False → preserves special characters and accents
    # indent=4           → formats with readable indentation

print(f"✓ Saved to JSON: {json_filename}")

# Reading it back
with open(json_filename, "r", encoding="utf-8") as file:
    loaded_books = json.load(file)

print(f"  Read from JSON: {len(loaded_books)} items")
print(f"  First: {loaded_books[0]['title'][:40]}...")


# ============================================================
# 2. SAVING TO CSV
# ============================================================
# CSV is ideal for opening in Excel, Google Sheets, pandas, etc.

csv_filename = "books.csv"

# "fields" are the dictionary keys (CSV header row)
fields = ["title", "price", "stars", "available"]

with open(csv_filename, "w", newline="", encoding="utf-8-sig") as file:
    # utf-8-sig → adds BOM so Excel correctly reads special characters
    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()    # writes the header row
    writer.writerows(books) # writes all data rows

print(f"\n✓ Saved to CSV: {csv_filename}")

# Reading it back
with open(csv_filename, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    csv_books = list(reader)

print(f"  Read from CSV: {len(csv_books)} items")
print(f"  First: {csv_books[0]['title'][:40]}...")

# ============================================================
# WHEN TO USE EACH FORMAT?
# ============================================================
# JSON  → complex/nested data, APIs, reusing in Python code
# CSV   → flat tabular data, Excel, pandas, data analysis
#
# Tip: if your data has lists inside lists (e.g. a product's tags),
# use JSON. If it's a flat table, use CSV.