import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://www.jumia.co.ke/computing/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
TOTAL_PAGES = 50
OUTPUT_DIR = "data/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_jumia_laptops.csv")

def scrape_jumia_products():
    """
    Scrapes product data from the Jumia Kenya computing section.
    
    Returns:
        pd.DataFrame: A DataFrame containing the raw scraped data.
    """
    all_data = []

    for page in range(1, TOTAL_PAGES + 1):
        print(f"Scraping page {page}/{TOTAL_PAGES}...")
        url = f"{BASE_URL}?page={page}#catalog-listing"
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()  # Raise an exception for bad status codes
        except requests.RequestException as e:
            print(f"Failed to fetch page {page}. Error: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("article", class_="prd")

        if not products:
            print(f"No products found on page {page}. Possibly the last page. Ending scrape.")
            break

        for product in products:
            name_tag = product.find("h3", class_="name")
            price_tag = product.find("div", class_="prc")
            old_price_tag = product.find("div", class_="old")
            discount_tag = product.find("div", class_="bdg _dsct")
            rating_tag = product.find("div", class_="rev")
            link_tag = product.find("a", class_="core")
            img_tag = product.find("img", class_="img")

            all_data.append({
                "product_name": name_tag.text.strip() if name_tag else None,
                "price": price_tag.text.strip() if price_tag else None,
                "old_price": old_price_tag.text.strip() if old_price_tag else None,
                "discount": discount_tag.text.strip() if discount_tag else None,
                "rating": rating_tag.text.strip() if rating_tag else None,
                "product_url": "https://www.jumia.co.ke" + link_tag['href'] if link_tag else None,
                "image_url": img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else None,
            })
        
        time.sleep(1) # Be respectful to the server

    return pd.DataFrame(all_data)

if __name__ == "__main__":
    print("Starting the Jumia data scraper...")
    
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    raw_df = scrape_jumia_products()
    
    if not raw_df.empty:
        raw_df.to_csv(OUTPUT_FILE, index=False)
        print(f"Scraping complete. {len(raw_df)} records saved to {OUTPUT_FILE}")
    else:
        print("Scraping finished with no data.")
        