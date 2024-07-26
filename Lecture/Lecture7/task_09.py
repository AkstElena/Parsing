# пример для работы с выпадающим меню

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


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

# Найдите выпадающее меню и выберите нужную опцию
dropdown = driver.find_element(By.ID, "dropdown-menu")
select = Select(dropdown)
# объект позволяющий взаимодействовать с выпадающим меню
select.select_by_visible_text("Option 2")
# выбираем текст в выпадающем меню
driver.quit()

