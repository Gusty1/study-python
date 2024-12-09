"""
體驗 Selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定無頭模式
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://ezpost.post.gov.tw/")

cookies = driver.get_cookies()
print(type(cookies))
print("Cookies:", cookies)
for i in cookies:
    print(i['value'])

driver.quit()
