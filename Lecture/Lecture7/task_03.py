from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)
url = "https://www.imdb.com/chart/top"
chrome_option = Options()
chrome_option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_option)

driver.get(url)

movie_title_elements = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item h3")
rating_elements = driver.find_elements(By.CSS_SELECTOR, "span.ipc-rating-star--rating")
titles = [element.text for element in movie_title_elements]
ratings = [element.text for element in rating_elements]
for i in range(10):
    print("Rank {}: {} ({} stars)".format(i + 1, titles[i], ratings[i]))
driver.quit()
