import csv

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)
url = "http://quotes.toscrape.com/page/1/"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

# Переход на первую страницу веб-сайта
driver.get(url)
# Инициализация пустого списка для хранения цитат
quotes = []
while True:
    # Поиск всех цитат на странице с помощью xpath
    quote_elements = driver.find_elements(By.XPATH, '//div[@class="quote"]')
    # Извлечение текста каждой цитаты
    for quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH, './/span[@class="text"]').text
        author = quote_element.find_element(By.XPATH, './/span/small[@class="author"]').text
        quotes.append({"quote": quote, "author": author})
        # Проверка наличия следующей кнопки
    next_button = driver.find_elements(By.XPATH, '//li[@class="next"]/a')
    if not next_button:
        break
    # Нажатие следующей кнопки
    next_button[0].click()
    # Ожидание загрузки страницы
    time.sleep(1)
    # Закрытие браузера
driver.close()

with open('quotes.csv', 'w', newline='', encoding='UTF-8') as f:
    write = csv.DictWriter(f, fieldnames=["quote", "author"])
    write.writeheader()
    write.writerows(quotes)


# Вывод цитат

