import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup driver
service = Service("C:\\Program Files (x86)\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Category -> Product type mapping
category_product_map = {
    "Agricultural Equipment": ["seed planter", "knapsack", "drone"],
    "Electronics": ["smart weather stations", "wireless solar camera", "soil moisture sensors"],
    "Chemical": ["fertilizers", "herbicides", "insecticide"]
}

all_products = []

# Visit site
driver.get("https://www.made-in-china.com/")
time.sleep(3)

# Scrape for each category and product type
for category, product_types in category_product_map.items():
    for product_type in product_types:
        print(f"\n🔍 Searching for: {product_type} in {category}")
        try:
            search_box = driver.find_element(By.NAME, "word")
            search_box.clear()
            search_box.send_keys(f"{category} {product_type}")
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)

            product_count = 0

            while product_count < 1000:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.prod-list > div"))
                )
                product_cards = driver.find_elements(By.CSS_SELECTOR, "div.prod-list > div")

                for prod in product_cards:
                    try:
                        product_info = {
                            "Product Name": "",
                            "Price": "",
                            "Company Name": "",
                            "Product Type": product_type,
                            "Category": category,
                            "Product Property": ""
                        }

                        # Product Name
                        try:
                            name_elem = prod.find_element(By.CSS_SELECTOR, "h2.product-name > a")
                            product_info["Product Name"] = name_elem.text.strip()
                        except:
                            pass

                        # Price
                        try:
                            price_elem = prod.find_element(By.CSS_SELECTOR, "div.product-property > div.info.price-info")
                            product_info["Price"] = price_elem.text.strip()
                        except:
                            pass

                        # Company Name
                        try:
                            company_elem = prod.find_element(By.CSS_SELECTOR, "div.pro-extra > ul > li:nth-child(1) > div")
                            product_info["Company Name"] = company_elem.text.strip()
                        except:
                            pass

                        # Product Property
                        try:
                            property_container = prod.find_element(By.CSS_SELECTOR, "div.extra-property.cf")
                            props = property_container.find_elements(By.CSS_SELECTOR, "dl")
                            product_properties = []
                            for prop in props:
                                try:
                                    title = prop.find_element(By.TAG_NAME, "dt").text.strip()
                                    value = prop.find_element(By.TAG_NAME, "dd").text.strip()
                                    product_properties.append(f"{title}: {value}")
                                except:
                                    continue
                            product_info["Product Property"] = "; ".join(product_properties)
                        except:
                            pass

                        all_products.append(product_info)
                        product_count += 1

                        if product_count >= 1000:
                            break
                    except:
                        continue

                # Try to go to the next page
                try:
                    next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.LINK_TEXT, "Next"))
                    )
                    next_button.click()
                    time.sleep(3)
                except:
                    print(f"No more pages for {product_type} in {category}.")
                    break

        except Exception as e:
            print(f"Error searching for {product_type}:", e)

# Save all results to CSV
keys = all_products[0].keys() if all_products else []
with open("product_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(all_products)

print(f"✅ Scraping complete. {len(all_products)} products saved to 'product_results.csv'.")
driver.quit()
