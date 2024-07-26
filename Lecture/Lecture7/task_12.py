# пример для обхода captcha

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

# Использование headless браузера, чтобы избежать механизмов обнаружения ботов
options = Options()
options.headless = True

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome(options=options)

# Загрузка веб-сайта
driver.get("https://example.com/")

# Решение задачи CAPTCHA
captcha_element = driver.find_element(By.ID, "captcha")
captcha_image_src = captcha_element.get_attribute("src")
captcha_image_data = requests.get(captcha_image_src).content

# Использование OCR для извлечения текста из изображения CAPTCHA
captcha_text = "CAPTCHA_SOLUTION"

# Ввод текста CAPTCHA в форму
captcha_input = driver.find_element(By.ID, "captcha_input")
captcha_input.send_keys(captcha_text)

# Отправка формы
submit_button = driver.find_element(By.ID, "submit_button")
submit_button.click()

# Ожидание загрузки страницы перед извлечением данных
time.sleep(3)

# Извлечение данных со страницы
data = driver.find_elements(By.XPATH, "//div[@class='data-element']")
data_list = []
for item in data:
    data_list.append(item.text)

# Закрытие веб-драйвера
driver.quit()
# Вывод извлеченных данных
print(data_list)
