from bs4 import BeautifulSoup
import urllib.parse
import requests
import re
import json

# print(link)
url = 'http://books.toscrape.com/catalogue/page-2.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)