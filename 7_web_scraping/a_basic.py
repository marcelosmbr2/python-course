# ============================================================
# WEB SCRAPING - BASICS
# ============================================================
# Web scraping = automatically extracting data from websites
# Think of it as "copying" information from a page, but via code
#
# MAIN TOOLS:
#   requests        → makes the HTTP request (fetches the page HTML)
#   BeautifulSoup   → parses and navigates the returned HTML
#
# INSTALL:
#   pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# ============================================================
# 1. MAKING AN HTTP REQUEST
# ============================================================
# requests.get() fetches the content of a URL
# It's like a browser asking a server for a page

url = "https://books.toscrape.com"  # practice site made for scraping
response = requests.get(url)

print(response.status_code)   # 200 = success, 404 = not found
print(response.text[:500])    # raw HTML of the page (first 500 chars)


# ============================================================
# 2. PARSING HTML WITH BEAUTIFULSOUP
# ============================================================
# BeautifulSoup turns raw HTML into something we can navigate
# "html.parser" is Python's built-in parser (nothing extra to install)

soup = BeautifulSoup(response.text, "html.parser")

# HTML structure we'll be navigating:
# <html>
#   <body>
#     <h1 class="title">Hello</h1>
#     <p id="description">Some text here</p>
#     <a href="/link">Click me</a>
#   </body>
# </html>


# ============================================================
# 3. SELECTING ELEMENTS
# ============================================================

# --- find() → returns the FIRST matching element ---
first_h1 = soup.find("h1")
print(first_h1)          # <h1>Text</h1>
print(first_h1.text)     # just the inner text: "Text"

# Search by CSS class
element = soup.find("p", class_="intro")

# Search by id
element = soup.find("div", id="content")

# --- find_all() → returns ALL matching elements as a list ---
all_links = soup.find_all("a")
for link in all_links:
    print(link.text)           # link text
    print(link.get("href"))    # href attribute (URL)

# Find all elements of a specific class
articles = soup.find_all("article", class_="product")


# ============================================================
# 4. EXTRACTING ATTRIBUTES
# ============================================================
# HTML elements have attributes: href, src, class, id, etc.

# Option 1: .get("attribute") → returns None if missing (safe)
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)

# Option 2: element["attribute"] → raises error if missing (careful!)
image = soup.find("img")
src = image["src"]