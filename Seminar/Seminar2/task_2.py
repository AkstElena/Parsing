"""
Напишите сценарий на языке Python, чтобы получить ссылки на релизы фильмов со страницы "International Box Office" на сайте Box Office Mojo.
Сохраните ссылки в списке и выведите список на консоль.

Требования:

- Используйте библиотеку requests для запроса веб-страницы.
- Используйте Beautiful Soup для парсинга HTML-содержимого веб-страницы.
- Найдите все ссылки в колонке #1 Release веб-страницы.
- Используйте библиотеку urllib.parse для объединения ссылок с базовым URL.
- Сохраните ссылки в списке и выведите список на консоль.
"""

from bs4 import BeautifulSoup
import urllib.parse
import requests
import pandas as pd

response = requests.get("https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab")
# print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soap.prettify())

release_links = []
for link in soup.find_all('td', {'class': 'a-text-left mojo-field-type-release mojo-cell-wide'}):
    a_tag = link.find('a')
    if a_tag:
        release_links.append(a_tag.get('href'))

# print(release_link)

url_joined = [urllib.parse.urljoin('https://www.boxofficemojo.com', link) for link in release_links]

table = soup.find('table', {'class': 'a-bordered'})
headers = [header.text.strip() for header in table.find_all('th') if header.text]

data = []
for row in table.find_all('tr'):
    row_data = {}
    cells = row.find_all('td')
    if cells:
        row_data[headers[0]] = cells[0].find('a').text if cells[0].find('a') else ''
        row_data[headers[1]] = cells[1].find('a').text if cells[1].find('a') else ''
        row_data[headers[2]] = int(cells[2].text)
        row_data[headers[3]] = cells[3].find('a').text if cells[3].find('a') else ''
        row_data[headers[4]] = cells[4].find('a').text.strip() if cells[4].find('a') else ''
        row_data[headers[5]] = int(cells[5].text[1:].replace(',', ''))
        data.append(row_data)


df = pd.DataFrame(data)
df.to_json('task2.json')
df.to_csv('task2.csv')

print(df)
