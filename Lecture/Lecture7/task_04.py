# Пример реализации панагинации

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com/movies")

next_button_locator = (By.XPATH, '//a[@class="next"]')  # тег для поиска ссылки на следующую страницу

current_page = 1
while True:
    print(f"Scraping page {current_page}...")
    try:
        next_button = driver.find_element(*next_button_locator)
        next_button.click()
        current_page += 1
    except NoSuchElementException:
        break
driver.quit()
