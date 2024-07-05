# Импорт необходимых библиотек
import requests
import json

# Определение конечной точки API
url = "http://openlibrary.org/search.json"

# Определение темы поиска и параметров для запроса API
subject = "Artificial intelligence"
params = {"subject": subject, "limit": 10}

# Отправка запроса API с помощью метода requests.get
response = requests.get(url, params=params)

# Проверка кода состояния ответа для подтверждения успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
else:
    print("Запрос API отклонен с кодом состояния:", response.status_code)

# Загрузка данных ответа в виде объекта JSON
data = json.loads(response.text)

# Доступ к списку книг из данных ответа
books = data["docs"]

# Извлечение названия книги, автора и темы.
for book in books:
    print("Title:", book["title"])
    print("Author:", book["author_name"])
    print("Subject:", book["subject"])
    print("\n")
