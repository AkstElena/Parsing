import requests
from lxml import html

from pymongo import MongoClient


def insert_to_db(list_movies):
    client = MongoClient('mongodb://localhost:27017/')
    db = client["imdb_movies"]
    collection = db["top_movies"]
    collection.insert_many(list_movies)
    client.close()


all_movies = []

resp = requests.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm', headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
})

tree = html.fromstring(html=resp.content)

movies = tree.xpath("//ul[contains(@class, 'ipc-metadata-list')]/li")


def get_titlemeter(list_element):
    try:
        return (list_element[0].split()[1])
    except:
        return "no change"


def get_position_change(list_element):
    try:
        return int(list_element[0])
    except:
        return 0


for movie in movies:
    m = {
        'name': movie.xpath('.//h3[@class="ipc-title__text"]/text()')[0],
        'release_year': int(movie.xpath(".//div[contains(@class, 'cli-title-metadata')]/span/text()")[0]),
        'position': int(movie.xpath(".//div[contains(@aria-label, 'Ranking')]/text()")[0]),
        'titlemeter': get_titlemeter(movie.xpath(".//span[contains(@aria-label, 'Moved')]/@aria-label")),
        'position_change': get_position_change(movie.xpath(".//span[contains(@aria-label, 'Moved')]/text()"))
    }

    all_movies.append(m)

insert_to_db(all_movies)
# print(all_movies)
print(len(all_movies))
