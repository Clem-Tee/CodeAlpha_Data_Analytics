import pandas as pd
import numpy as np
import re
import os

RAW_DATA_PATH = "data/raw/raw_jumia_laptops.csv"
PROCESSED_DATA_PATH = "data/processed/cleaned_jumia_laptops.csv"

def clean_price(price_str):
    """Extracts the first number from a price string (handles ranges like '460 - 1998')."""
    if isinstance(price_str, str):
        # Remove currency and commas
        price_str = price_str.replace("KSh", "").replace(",", "").strip()
        # Find the first sequence of digits
        match = re.search(r"^\d+", price_str)
        if match:
            return int(match.group(0))
    return 0

def clean_and_enrich_data(df):
    """
    Cleans the raw Jumia product data and adds new, useful columns.

    Args:
        df (pd.DataFrame): The raw data DataFrame.

    Returns:
        pd.DataFrame: The cleaned and enriched DataFrame.
    """
    # 1. Clean Price Columns
    df['price'] = df['price'].apply(clean_price)
    df['old_price'] = df['old_price'].apply(clean_price)

    # 2. Clean Discount and Impute Old Price
    df['discount_scraped'] = pd.to_numeric(df['discount'].str.replace('%', '', regex=False), errors='coerce')
    
    mask = (df['old_price'] == 0) & (df['discount_scraped'].notna())
    df.loc[mask, 'old_price'] = (
        df.loc[mask, 'price'] / (1 - (df.loc[mask, 'discount_scraped'] / 100))
    ).round(0).astype(int)

    # 3. Recalculate a standardized discount percentage
    df['discount_percent'] = (
        ((df['old_price'] - df['price']) / df['old_price']) * 100
    ).replace([np.inf, -np.inf], 0).fillna(0).round(1)
    df.loc[df['discount_percent'] < 0, 'discount_percent'] = 0 # Correct any negative discounts

    # 4. Filter for actual Laptops/Computers
    computer_keywords = [
        "laptop", "asus", "macbook", "notebook", "chromebook", "elitebook", "thinkpad", 
        "inspiron", "vivobook", "ideapad", "probook", "latitude", "envy", 
        "pavilion", "surface", "xps", "spectre", "zenbook", "gram", "swift", 
        "aspire", "imac", "aio", "all-in-one", "desktop", "pc", "omen"
    ]
    
    def is_computer(text):
        if isinstance(text, str):
            return any(kw in text.lower() for kw in computer_keywords)
        return False

    name_filter = df['product_name'].apply(is_computer)
    url_filter = df['product_url'].apply(is_computer)
    df = df[name_filter | url_filter].copy()

    # 5. Extract Brand
    def extract_brand(name):
        if not isinstance(name, str):
            return "UNKNOWN"
        name_lower = name.lower()
        if 'hp' in name_lower or 'elitebook' in name_lower or 'probook' in name_lower or 'pavilion' in name_lower or 'omen' in name_lower:
            return "HP"
        if 'lenovo' in name_lower or 'thinkpad' in name_lower or 'ideapad' in name_lower:
            return "Lenovo"
        if 'dell' in name_lower or 'latitude' in name_lower or 'xps' in name_lower:
            return "Dell"
        if 'apple' in name_lower or 'macbook' in name_lower or 'imac' in name_lower:
            return "Apple"
        if 'asus' in name_lower:
            return "Asus"
        if 'toshiba' in name_lower:
            return "Toshiba"
        if 'acer' in name_lower:
            return "Acer"
        if 'samsung' in name_lower:
            return "Samsung"
        return name.split()[0].upper()

    df['brand'] = df['product_name'].apply(extract_brand)

    # 6. Extract Rating Score and Count
    def split_rating(value):
        if isinstance(value, str):
            match = re.search(r'([\d.]+)\s+out of 5.*?\((\d+)\)', value)
            if match:
                return float(match.group(1)), int(match.group(2))
        return None, 0

    df[['rating_score', 'rating_count']] = df['rating'].apply(lambda x: pd.Series(split_rating(x)))
    df['rating_score'] = df['rating_score'].fillna(0)
    df['rating_count'] = df['rating_count'].fillna(0).astype(int)

    # 7. Final Column Selection and Cleanup
    final_cols = [
        'product_name', 'brand', 'price', 'old_price', 'discount_percent',
        'rating_score', 'rating_count', 'product_url'
    ]
    df_cleaned = df[final_cols].copy()
    
    # Remove duplicates based on product_url
    df_cleaned = df_cleaned.drop_duplicates(subset=['product_url'])
    
    # Remove items with a price of 0 as they are likely errors
    df_cleaned = df_cleaned[df_cleaned['price'] > 0]
    
    df_cleaned = df_cleaned.reset_index(drop=True)
    
    return df_cleaned

if __name__ == "__main__":
    print("Starting data cleaning process...")
    
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: Raw data file not found at {RAW_DATA_PATH}. Please run scraper.py first.")
    else:
        raw_df = pd.read_csv(RAW_DATA_PATH)
        cleaned_df = clean_and_enrich_data(raw_df)
        
        # Ensure the processed data directory exists
        os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
        
        cleaned_df.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"Cleaning complete. {len(cleaned_df)} records saved to {PROCESSED_DATA_PATH}")
        