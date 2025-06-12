from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random
import time
import string

chrome_driver_path = "/usr/local/bin/chromedriver"

# Generate random worker name
def generate_worker_name(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

worker_name = generate_worker_name()
wallet = "XcufdyxZtL4JUjALZfTq6pCrxyTt2Hy2Zu"

chrome_options = Options()
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-tools")
chrome_options.add_argument("--no-default-browser-check")
chrome_options.add_argument("--no-first-run")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            window.chrome = {
                runtime: {},
            };
        """
    })

    print("Starting Unmineable mining operation...")

    def human_like_delay(min=1, max=3):
        time.sleep(random.uniform(min, max))

    base_url = f"https://webminer.pages.dev?algorithm=cwm_randomx&host=randomx.unmineable.com&port=3333&worker=DOGE:{wallet}.{worker_name}&password=x&workers=32"
    
    driver.get(base_url)
    human_like_delay()

    while True:
        hashrate = driver.find_element(By.CSS_SELECTOR, "span#hashrate strong").text
        print(f"{time.ctime()} - Hashrate: {hashrate}")
        time.sleep(5)

except Exception as e:
    print(f"Critical error: {str(e)}")
    if 'driver' in locals():
        driver.quit()
