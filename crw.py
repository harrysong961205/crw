from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


url = "https://www.teamblind.com/kr/post/%EC%B9%A8%EC%83%98%EB%B3%B4%ED%86%A1%EC%8A%A4-%ED%9A%A8%EA%B3%BC%EB%B3%B4%EC%8B%A0%EB%B6%84-Lu5A3gtT"

browser = webdriver.Chrome(options=options)
browser.get(url)
time.sleep(1)
image = browser.save_screenshot("screenshots/scr1.png")
#print(browser.page_source)