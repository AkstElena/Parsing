from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
from urllib.parse import unquote_plus

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)

chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
# chrome_option.add_argument('--ignore-certificate-errors-spki-list')
chrome_option.add_argument('start-maximized')  # хром на весь экран

driver = webdriver.Chrome(options=chrome_option)
url = 'https://www.chitai-gorod.ru/'
search_category = 'фантастика'  # необходимая категория для поиска
pages_count = 4  # количество страниц на сайте для вывода данных

driver.get(url)
# Находим поле для поиска
search_box = driver.find_element(By.XPATH, "//input[@class='header-search__input']")
# вставляем в это поле слово которое хотим найти
search_box.send_keys(search_category)
# нажатие кнопки поиска
search_box.submit()
# ожидаем загрузки страницы
time.sleep(5)

# проверка что слово есть в заголовке, значит открылась нужная страница
search_results = driver.current_url.split('=')[-1]
res = unquote_plus(search_results, encoding="utf-8")
assert search_category in res
# time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
# print(driver.get_screenshot_as_file('screen.png'))

url = driver.current_url  # сохраняем текущий адрес страницы с поиском (так как ссылки в панагинаторе кривые)
books_data = {}
while pages_count - 1 > 0:
    products_list = driver.find_elements(By.XPATH, "//article[@class='product-card product-card product']")
    for product in products_list:
        try:
            book_title = product.find_element(By.XPATH, ".//div[@class='product-title__head']")
            title = book_title.text.strip().replace(r"\\", "")
        except:
            title = 'отсутствуют данные по названию'
        try:
            book_author = product.find_element(By.XPATH, ".//div[@class='product-title__author']")
            author = book_author.text.strip()
        except:
            author = 'отсутствуют данные по автору'
        try:
            book_price = product.find_element(By.XPATH, ".//div[contains(@class,'product-price__value')]")
            price = int(book_price.text.strip().replace(' ', '').replace('₽', ''))
        except:
            price = 'отсутствуют данные по цене'
        books_data[title] = {'author': author, 'price': price}
    # ищем номер следующей страницы поиска
    try:
        next_page_numbers = driver.find_elements(By.XPATH, '//a[@class="pagination__button pagination__button--icon"]')
        next_page_number = next_page_numbers[1].get_attribute('href').split('=')[-1]
    except:
        next_page_number = driver.find_element(By.XPATH, '//a[@class="pagination__button pagination__button--icon"]') \
            .get_attribute('href').split('=')[-1]
    if not next_page_number:
        break
    page_url = url + '&page=' + next_page_number  # получаем следующую страницу поиска
    driver.get(page_url)  # переходим на следующую страницу поиска
    # Ожидание загрузки страницы
    time.sleep(1)
    pages_count -= 1

with open('books_data.json', 'w', encoding='UTF-8', newline='') as f:
    json.dump(books_data, f, ensure_ascii=False, indent=4)
print('Данные сохранены в файл books_data.json')

driver.close()
