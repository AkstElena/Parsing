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

client = MongoClient('mongodb://localhost:27017/')
db = client['homework']
collection = db['hw_3_books']

# вывод первой записи в коллекции
all_docs = collection.find()
first_doc = all_docs[0]
# print(first_doc)

# вывод объекта json
pretty_json = json.dumps(first_doc, indent=4, default=str)
# print(pretty_json)


count = collection.count_documents({})
print(f"Общее количество книг, информация о которых выгружена с сайта =  {count}")
print('--------------------------')
print(f'Количество книг с рейтингом 5: {collection.count_documents({"Rating": 5})}')
print('--------------------------')
projection = {'Name': 1, 'Category': 1, '_id': 0}
books = collection.find({'Category': 'Science Fiction'}, projection)
books_count = collection.count_documents({'Category': 'Science Fiction'})
print(f'Количество книг в жанре Science Fiction: {books_count}')

for book in books:
    pretty_book = json.dumps(book, indent=4, default=str)
    print(pretty_book)
print('--------------------------')
projection_with_price = {'Name': 1, 'Price (Euro)': 1, 'Quantity_in_stock': 1, '_id': 0}
query = {'Price (Euro)': {'$lt': 20}, 'Quantity_in_stock': {'$gte': 19}}
books = collection.find(query, projection_with_price)
books_count = collection.count_documents(query)
print(f'Количество книг в жанре c ценой менее 20 фунтов стерлингов и количеством более или равном 19: {books_count}')
for book in books:
    pretty_book = json.dumps(book, indent=4, default=str)
    print(pretty_book)
print('--------------------------')


query = {'Name': {'$regex': 'woman', '$options': 'i'}}
books = collection.find(query, projection)
books_count = collection.count_documents(query)
print(f'Количество книг со словом Women в названии: {books_count}')
for book in books:
    pretty_book = json.dumps(book, indent=4, default=str)
    print(pretty_book)


