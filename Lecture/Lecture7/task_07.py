# пример для динамических страниц


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)
url = "https://www.example.com"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

# Переход на первую страницу веб-сайта
driver.get(url)


# Выполнение JavaScript для взаимодействия со страницей
result = driver.execute_script("return document.title")
print(result)
driver.quit()


