# api/scraper.py
import asyncio
from playwright.async_api import async_playwright

async def scrape_product_info(product_name: str):
    """
    Scrapes product information from Google Shopping using Playwright.
    """
    products = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            # Navigate to Google Shopping and search for the product
            await page.goto(f"https://www.google.com/shopping?q={product_name}")
            
            # Wait for the product cards to be visible
            await page.wait_for_selector('div[data-ved] h3', timeout=5000)

            # Extract data from each product card
            product_cards = await page.query_selector_all('div[data-ved]')

            for card in product_cards:
                try:
                    name_element = await card.query_selector('h3')
                    brand_element = await card.query_selector('.H9If7d')
                    price_element = await card.query_selector('.a8Pemb')
                    
                    name = (await name_element.text_content()).strip() if name_element else 'N/A'
                    brand = (await brand_element.text_content()).strip() if brand_element else 'N/A'
                    price = (await price_element.text_content()).strip() if price_element else 'N/A'
                    
                    products.append({
                        'product_name': name,
                        'brand': brand,
                        'price': price,
                        'total_weight': 'N/A' # Weight is often not directly available
                    })
                except Exception as e:
                    print(f"Error scraping a product card: {e}")
                    continue

        except Exception as e:
            print(f"An error occurred during scraping: {e}")
        finally:
            await browser.close()

    return products