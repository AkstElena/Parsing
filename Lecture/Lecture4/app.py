import requests
from lxml import html
from pymongo import MongoClient


def insert_to_db(list_movies):
    client = MongoClient("mongodb+srv://petr:4l5qU03ylDv@cluster0.sqjshf7.mongodb.net/?retryWrites=true&w=majority")
    db = client["imdb_movies"]
    collection = db["top_movies"]
    collection.insert_many(list_movies)
    client.close()


all_movies = []

resp = requests.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm', headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
})

tree = html.fromstring(html=resp.content)

movies = tree.xpath("//table[@data-caller-name='chart-moviemeter']/tbody/tr")


def get_titlemeter(list_element):
    try:
        return (list_element[0].split()[-1])
    except:
        return "no change"


def get_position_change(list_element):
    try:
        return (int(list_element[0].strip()[:-1]))
    except:
        return 0


for movie in movies:
    m = {
        'name': movie.xpath(".//td[contains(@class, 'titleColumn')]/a/text()")[0],
        'release_year': int(movie.xpath(".//td[contains(@class, 'titleColumn')]/span/text()")[0][1:-1]),
        'position': int(movie.xpath(".//td[contains(@class, 'titleColumn')]/div/text()")[0].split()[0]),
        'titlemeter': get_titlemeter(movie.xpath(".//td[contains(@class, 'titleColumn')]/div/span/span/@class")),
        'position_change': get_position_change(movie.xpath(".//td[contains(@class, 'titleColumn')]/div/span/text()[2]"))
    }

    all_movies.append(m)

insert_to_db(all_movies)
print(len(all_movies))
