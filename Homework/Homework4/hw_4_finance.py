"""
Урок 4. Парсинг HTML. XPath
Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:
Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.
"""

import requests
from lxml import html
import pandas as pd


def error_find(my_string, index_number):
    try:
        return row.xpath(my_string)[index_number]
    except:
        return '0'


url = 'https://finance.yahoo.com/trending-tickers/'
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/108.0.0.0 Safari/537.36'})

tree = html.fromstring(response.content)

table_rows = tree.xpath('//*[@id="list-res-table"]/div[1]/table/tbody/tr')

list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_data.append({
        'Symbol': row.xpath(".//td/a/text()")[0].strip(),
        'Name': columns[0].strip(),
        'Last Price': int(row.xpath(".//td/fin-streamer/text()")[0].replace(',', '').replace('.', '').strip()),
        'MarketTime': row.xpath(".//td/fin-streamer/text()")[1].strip(),
        'Change': float(row.xpath(".//td/fin-streamer/span/text()")[0].strip()),
        'Change %': float(row.xpath(".//td/fin-streamer/span/text()")[1][:-1].strip()),
        'Volume': int(row.xpath(".//td/fin-streamer/text()")[2].replace('.', '').replace(',', '').replace('M', '000000')
                      .replace('B', '000000000').replace('T', '000000000000').strip()),
        'Market Cap': int(error_find(".//td/fin-streamer/text()", 3).replace('.', '').replace(',', '')
                          .replace('M', '000000').replace('B', '000000000').replace('T', '000000000000').strip())
    })

# print(list_data)

df = pd.DataFrame(list_data)
print(df)
df.to_csv('hw_4_finance.csv')
