# пример для работы с модальным окном

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)
url = "https://duckduckgo.com/"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

# Переход на первую страницу веб-сайта
driver.get(url)

# Поиск строки поиска и ввод поискового запроса
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Selenium books")

# Поиск кнопки поиска и нажатие на нее
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

# Поиск выпадающего меню "Время" и щелчок по нему
time_dropdown = driver.find_element(By.XPATH, "//*[@id='links_wrapper']/div[1]/div[1]/div/div[3]/a")
time_dropdown.click()

# Поиск опции "За последний месяц" в выпадающем меню времени и щелчок по ней
time_last_month = driver.find_element(By.XPATH, "*//a[@data-value='m']")
time_last_month.click()

more_btn = driver.find_element(By.XPATH, "//button[@id='more-results']")
more_btn.click()

# Поиск всех результатов на странице
results = driver.find_elements(By.XPATH, "//li[@class='wLL07_0Xnd1QZpzpfR4W']")
result_data = []

# Извлечение заголовка и URL каждого результата

for result in results:
    result_title = result.find_element(By.XPATH, ".//h2[@class='LnpumSThxEWMIsDdAT17 CXMyPcQ6nDv47DKFeywM']/a/span").text
    result_url = result.find_element(By.XPATH, './/a[@data-testid="result-title-a"]').get_attribute("href")
    result_data.append([result_title, result_url])
driver.quit()

# Запись данных в файл CSV
with open("duckduckgo_results.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Result Title", "URL"])
    writer.writerows(result_data)
