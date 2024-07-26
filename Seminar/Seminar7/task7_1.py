from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# класс для указания типа селектора
from selenium.webdriver.common.by import By
# класс для ожидания наступления события
from selenium.webdriver.support.ui import WebDriverWait
# включает проверки, такие как видимость элемента на странице, доступность элемента для отклика и т.п.
from selenium.webdriver.support import expected_conditions as EC
# ошибки в selenium
from selenium.webdriver.chrome.options import Options
# работа со всеми возможными функциями
import time

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)

chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
# chrome_option.add_argument('--ignore-certificate-errors-spki-list')
chrome_option.add_argument('start-maximized')  # хром на весь экран

driver = webdriver.Chrome(options=chrome_option)
url = 'https://www.youtube.com/@progliveru/videos'
driver.get(url)

# ожидаем подгрузку всех элементов тела
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

scroll_pause = 2
last_height = driver.execute_script('return document.documentElement.scrollHeight')  # высота экрана

while True:
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    time.sleep(scroll_pause)
    page_height = driver.execute_script('return document.documentElement.scrollHeight')
    if last_height == page_height:
        break
    last_height = page_height
    print(f'Высота экрана: {last_height}')

print(f'Высота экрана: {page_height}')

driver.quit()
