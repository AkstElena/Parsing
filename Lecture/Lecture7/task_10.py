# пример для работы с модальным окном

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
url = "https://www.example.com/dropdown-menu"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

# Переход на первую страницу веб-сайта
driver.get(url)

# Нахождение триггера модального окна и клик на нем, чтобы открыть модальное окно
modal_trigger = driver.find_element(By.ID, "modal-trigger")
modal_trigger.click()
# Ожидание отображения модального окна
modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal")))
# Взаимодействовать с модальным окном (например, заполнение формы)
modal_input = modal.find_element(By.ID, "modal-input")
modal_input.send_keys("Hello, World!")
# Закрытие модального окна
modal_close = modal.find_element(By.ID, "modal-close")
modal_close.click()
# Закрытие браузера
driver.quit()

