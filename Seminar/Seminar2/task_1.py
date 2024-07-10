"""
https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab

- установите библиотеку Beautiful Soup.

- создайте новый сценарий Python и импортируйте библиотеку Beautiful Soup.

- напишите код для запроса веб-страницы https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab с помощью библиотеки requests.

- выведите HTML-содержимое веб-страницы в консоль.


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
import requests
import pandas as pd


response = requests.get("https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab")
# print(response.status_code)

soap = BeautifulSoup(response.content, 'html.parser')
print(soap.prettify())

