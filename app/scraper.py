from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_article(url):
    # Set up Selenium WebDriver with ChromeDriverManager
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Specify the correct path to the Chrome binary
    # Use Service for the driver, and pass options separately
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        main_content = soup.find('article') or soup.find('div', class_='content')
        title = soup.find('title').get_text() if soup.find('title') else 'Title not found'
        content = main_content.get_text(separator='\n').strip() if main_content else 'Content not found'

        return {'title': title, 'content': content}

    finally:
        driver.quit()
