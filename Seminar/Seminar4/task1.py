"""
https://worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1
Задание 1
Напишите сценарий на языке Python, который выполняет следующие задачи:
- отправляет HTTP GET-запрос на целевой URL и получает содержимое веб-страницы.
-  выполняет парсинг HTML-содержимого ответа с помощью библиотеки lxml.
-  используя выражения XPath, извлеките данные из первой строки таблицы.
- выведите извлеченные данные из первой строки таблицы в консоль.
"""

import requests
from lxml import html

url = 'https://worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1'
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

tree = html.fromstring(response.content)

table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")
columns = table_rows[0].xpath(".//td/text()")
# for col in columns:
#     print(col)

col_names = tree.xpath("//table[@class='records-table']/thead/tr/th/text()")
# for col in col_names:
#     print(col)
