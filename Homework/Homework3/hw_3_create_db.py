"""
Урок 3. Системы управления базами данных MongoDB и Кликхаус в Python
Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе.
https://www.mongodb.com/ https://www.mongodb.com/products/compass
Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB
и создайте базу данных и коллекции для их хранения.
Поэкспериментируйте с различными методами запросов.
Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения.
"""

from pymongo import MongoClient
import json

client = MongoClient()
db = client['homework']
collection = db['hw_3_books']

with open('books_all_page_with_category.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


chunk_size = 100
data_chunks = list(chunk_data(data, chunk_size))

for chunk in data_chunks:
    collection.insert_many(chunk)

