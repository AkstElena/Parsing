# пример для динамических страниц

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)
url = "https://quotes.toscrape.com/page/1/"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

# Переход на первую страницу веб-сайта
driver.get(url)

# ожидание загрузки элемента
wait = WebDriverWait(driver, 10)  # указываем максимальное время ожидания ответа
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".quote")))
# until - ожидание пока нужный элемент не появится на странице

# извлечение данных из элемента
quote = element.text
driver.quit()
