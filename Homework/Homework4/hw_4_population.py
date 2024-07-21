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
import pandas


def error_find(data, data_index):
    try:
        return data[data_index]
    except:
        return '0'


url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

tree = html.fromstring(response.content)

table_rows = tree.xpath('//*[@id="example2"]/tbody/tr')

list_data = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_data.append({
        'Country (or dependency)': row.xpath(".//td/a/text()")[0].strip(),
        'Population (2023)': int(columns[1].replace(',', '').strip()),
        'Yearly Change, %': float(columns[2].replace('%', '').strip()),
        'Net Change': int(columns[3].replace(',', '').strip()),
        'Density (P/Km²)': int(columns[4].replace(',', '').strip()),
        'Land Area (Km²)': int(columns[5].replace(',', '').strip()),
        'Migrants (net)': int(columns[6].replace(',', '').strip()),
        'Fert. Rate': float(columns[7].replace('N.A.', '0').strip()),
        'Med. Age': int(columns[8].replace('%', '').replace('.', '').strip()),
        'Urban Pop (%)': int(error_find(columns, 9).replace('%', '').replace('N.A.', '0').strip()),
        'World, %': float(error_find(columns, 10).replace('%', '').strip())
    })


# print(list_data)

df = pandas.DataFrame(list_data)
df.index = df.index + 1
print(df)
df.to_csv('hw_4_population.csv')
