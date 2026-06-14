# ============================================================
# WEB SCRAPING - CSS SELECTORS
# ============================================================
# BeautifulSoup also supports CSS selectors, which are more powerful and expressive

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# ============================================================
# 1. THE select() METHOD - CSS SELECTORS
# ============================================================
# select()     → returns a LIST of elements (like find_all)
# select_one() → returns the FIRST element (like find)

# By tag
headings = soup.select("h3")

# By CSS class  (.class-name)
products = soup.select(".product_pod")

# By id  (#id-name)
section = soup.select_one("#default")

# By attribute
links_with_href = soup.select("a[href]")
text_inputs = soup.select("input[type='text']")

# Descendant: elements INSIDE another element
# "article h3" = all h3 tags anywhere inside an article
article_headings = soup.select("article h3")

# Direct child: element DIRECTLY inside another
# "ul > li" = li tags that are direct children of ul
direct_items = soup.select("ul > li")

# Combining tag and class
# "p.price_color" = <p> tags with class price_color
prices = soup.select("p.price_color")

# Multiple selectors (comma = OR)
headings_and_prices = soup.select("h3, p.price_color")


# ============================================================
# 2. NAVIGATING THE HTML TREE
# ============================================================
# HTML is a tree: parent > child > grandchild
# BeautifulSoup lets you move up, down, and sideways

product = soup.select_one("article.product_pod")

# --- Children ---
print(product.children)         # generator of direct children
print(list(product.children))   # convert to list
print(product.contents)         # list of direct children

# All descendants (children, grandchildren, etc.)
for descendant in product.descendants:
    if descendant.name:         # .name is None for plain text nodes
        print(descendant.name)

# --- Parent ---
parent = product.parent
print(parent.name)              # tag name of the parent

# --- Siblings (same level) ---
next_el = product.next_sibling
prev_el = product.previous_sibling

# Siblings that are tags (skips whitespace/text nodes)
for sibling in product.next_siblings:
    if sibling.name:
        print(sibling.name)


# ============================================================
# 3. WORKING WITH TEXT
# ============================================================

# Get first <a> inside an <h3>
element = soup.select_one("h3 a")

# .text or .get_text() → extracts all inner text
print(element.text)
print(element.get_text())

# .get_text() has useful options:
print(element.get_text(strip=True))           # strips extra whitespace
print(element.get_text(separator=" | "))      # joins inner text nodes

# Example: getting text from an element with child elements
# <div><span>Price:</span> $50.00</div>
div = soup.find("div")
print(div.get_text(strip=True))   # "Price: $50.00"