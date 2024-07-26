from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# класс для указания типа селектора
from selenium.webdriver.common.by import By
# класс для ожидания наступления события
from selenium.webdriver.support.ui import WebDriverWait
# включает проверки, такие как видимость элемента на странице, доступность элемента для отклика и т.п.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import csv

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

try:
    driver.get(url)
    # ожидаем подгрузку всех элементов тела
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    scroll_pause = 2
    page_height = driver.execute_script('return document.documentElement.scrollHeight')  # высота экрана
    while True:
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
        time.sleep(scroll_pause)
        new_height = driver.execute_script('return document.documentElement.scrollHeight')
        if new_height == page_height:
            break
        page_height = new_height

    video_titles_xpath = "//*[@id='video-title-link']"
    metadata_xpath = "//div[@id='metadata-line']/span[1]"

    video_titles = driver.find_elements(By.XPATH, video_titles_xpath)
    metadata_elements = driver.find_elements(By.XPATH, metadata_xpath)

    video_data = {}
    for i in range(min(len(video_titles), len(metadata_elements))):
        # цикл проходит по индексам от 0 до минимальной длины между списками видео и метаданных,
        # чтобы избежать ошибки если они разной длины
        title = video_titles[i].text
        metadata_text = metadata_elements[i].text

        if '•' in metadata_text:
            view, time_ago = metadata_text.strip('•')
        else:
            view = metadata_text
            time_ago = 'Неизвестно'

        video_data[title] = {'views': view.strip(), 'published': time_ago.strip()}
    print(video_data)

except Exception as e:
    print(f'Произошла ошибка: {e}')
finally:
    driver.quit()



