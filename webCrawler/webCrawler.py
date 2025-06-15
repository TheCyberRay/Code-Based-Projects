from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import time

def get_links_with_selenium(url):
    try:
        # Set up WebDriver with automatic ChromeDriver installation
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new") #Alternative headless new

        # Pretend to be a real browser (helps avoid bot detection)
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")  # Maximize browser window
        options.add_argument("disable-infobars")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--remote-debugging-port=9222")

        # Automatically install and manage ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        print(f"Opening {url}...")  
        driver.get(url)
        
        time.sleep(5)

        # Wait for JavaScript-rendered links to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))

        # Print first 500 characters of page source (debugging step)
        print("\n--- Page Source Preview ---")
        print(driver.page_source[:500])
        print("\n--------------------------\n")

        # Extract all links
        links = set()
        for element in driver.find_elements(By.TAG_NAME, "a"):
            href = element.get_attribute("href")
            if href:
                links.add(href)

        driver.quit()

        return links

    except Exception as e:
        print(f"Error: {e}")
        return set()  # Return an empty set on error

# Usage
url = "add_your_website_link_here_"
links = get_links_with_selenium(url)

if links:
    print(f"\nFound {len(links)} links:")
    for link in links:
        print(link)
else:
    print("\nNo links found or an error occurred.")



