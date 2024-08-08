from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)
url = "https://www.amazon.com"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

driver.get(url)
print(driver.current_url)
# Находим поле для поиска
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# вставляем в это поле слово которое хотим найти
search_box.send_keys("laptops")
# нажатие кнопки поиска
search_box.submit()
print(driver.current_url)

# проверка что слово есть в заголовке, значит открылась нужная страница
assert "laptops" in driver.title

products = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
for product in products:
    print(product.text)
# print(div_element.get_attribute('class'))
