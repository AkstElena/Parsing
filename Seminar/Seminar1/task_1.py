"""
Задание 1
- использовать библиотеку requests в Python для отправки запросов GET, POST, PUT и DELETE на конечную точку REST API https://jsonplaceholder.typicode.com/posts/1.
- использовать методы requests.get(), requests.post(), requests.put() и requests.delete() для отправки соответствующих HTTP-запросов.
- проверить код состояния ответа и вывести текст ответа, если запрос был успешным.

Инструкции:
можно использовать предоставленный код в качестве отправной точки для своего решения.
"""

import requests


# отправка GET-запроса на конечную точку REST API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)


# отправка POST-запроса на конечную точку REST API
data = {"title": "GeekBrains", "body": "Scraping", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# проверка успешности выполнения запроса
if response.status_code == 201:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)


payload = {"field1": "value1", "field2": "value2"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)


response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# проверка успешности выполнения запроса
if response.status_code == 200:
    print("Успешный запрос!")
    # вывод текста ответа
    print(response.text)
else:
    print("Запрос не удался с кодом состояния:", response.status_code)
