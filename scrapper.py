from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import json
URL = "https://flexiclasses.com/japanese/jokes/"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

html = requests.get(URL)
soup = BeautifulSoup(html.text, 'html.parser')
table_content = soup.select('tbody tr')

# driver.get(URL)
# # content = driver.find_elements(By.CSS_SELECTOR, "div[class='listicle-slide-dek'] p")
print([c.select('td')[2].text + "(" + c.select('td')[3].text + "}" for c in table_content])

arr = [c.select('td')[2].text + "(" + c.select('td')[3].text + "}" for c in table_content]

jokes = {
    "JPN":arr
}

c_json = json.dumps(jokes, indent=4, ensure_ascii=False)

with open("json/JPN.json", "w", encoding='utf8') as file:
    file.write(c_json)

