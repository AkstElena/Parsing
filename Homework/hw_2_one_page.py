"""
Урок 2. Парсинг HTML. BeautifulSoup
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/
и извлечь информацию о всех книгах на сайте во всех категориях:
 название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

Затем сохранить эту информацию в JSON-файле.
"""
from bs4 import BeautifulSoup
import urllib.parse
import requests
import re
import json


def get_rating(text):
    match text:
        case "One":
            return 1
        case "Two":
            return 2
        case "Three":
            return 3
        case "Four":
            return 4
        case "Five":
            return 5
        case _:
            return 0


response = requests.get("http://books.toscrape.com")
# print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

books_links = []
for link in soup.find_all('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}):
    a_tag = link.find('a')
    if a_tag:
        books_links.append(a_tag.get('href'))
# print(books_links)

urls_joined = [urllib.parse.urljoin('http://books.toscrape.com', link) for link in books_links]
# print(urls_joined)

books_info = []
for link in urls_joined:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    book = soup.find('article', {'class': 'product_page'})
    book_dict = {}
    book_dict['Name'] = book.find('h1').text if book.find('h1') else ''
    book_dict['Price (Euro)'] = float(book.find('p', {'class': 'price_color'}).text[1:]) if book.find('p', {
        'class': 'price_color'}) else ''
    book_dict['Quantity_in_stock'] = int(
        re.findall(r'\d+', book.find('p', {'class': 'instock availability'}).text)[0]) if book.find(
        'p', {'class': 'instock availability'}) else ''
    book_dict['Rating'] = get_rating(book.find('p', {'class': 'star-rating'}).get('class')[1])
    book_dict['Description'] = book.find_all('p')[3].text.strip() if book.find_all('p')[3] else ''
    books_info.append(book_dict)

# print(books_info)


with open('books_one_page.json', 'w', encoding='utf-8') as f:
    json.dump(books_info, f, ensure_ascii=False, indent=4)
print('file created')
