"""

"""

# import requests # http запросы
# from bs4 import BeautifulSoup
# import urllib.parse
# from datetime import datetime
# import time
# import re # регулярные выражения
# import json # сюр строка - словарь

# def get_box_office_data():
#     url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'

#     # имитация устройства и браузера
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

#     response = requests.get(url, headers=headers) # запрашиваем урл и аргумент браузер
#     soup = BeautifulSoup(response.content, 'html.parser') # объект бс

#     # функ сбора ссылок
#     release_links = []
#     for link in soup.find_all('td', class_='a-text-left mojo-field-type-release mojo-cell-wide'):
#         a_tag = link.find('a')
#         if a_tag:
#             release_links.append(a_tag.get('href'))

#     url_joined = [urllib.parse.urljoin('https://www.boxofficemojo.com', link) for link in release_links]


#     data = []
#     for url in url_joined:
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         table = soup.find('div', class_='a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile')

#         if not table:
#             continue

#         rows = table.find_all('div', class_='a-section a-spacing-none')

#         row_data = {}
#         for row in rows:
#             key = row.find('span').text.strip()
#             spans = row.find_all('span')
#             if len(spans) > 1:
#                 value = spans[1].text.strip()
#                 if key == 'Opening':
#                     value = int(re.sub('[^0-9]', '', value))
#                 elif key == 'Release Date':
#                     value = value
#                 elif key == 'Running Time':
#                     try:
#                         time_parts = re.findall(r'\d+', value)
#                         hours, minutes = map(int, time_parts)
#                         value = hours * 3600 + minutes * 60
#                     except ValueError:
#                         continue
#                 elif key == 'Genres':
#                     value = [genre.strip() for genre in value.split(',') if genre.strip()]
#                 elif key == 'In Release':
#                     value = re.sub(r'[^\d]', '', value)
#                 elif key == 'Widest Release':
#                     value = int(re.sub('[^0-9]', '', value))

#                 row_data[key] = value

#         if row_data:
#             data.append(row_data)
#         #time.sleep(1)

#     return data

# def save_data_to_json(data, filename='box_office_data.json'):
#     with open(filename, 'w', encoding='utf=8') as f:
#         json.dump(data, f, indent=4)

# def main():
#     data = get_box_office_data()
#     save_data_to_json(data)

# if __name__ == "__main__":
#     main()


import requests  # Используется для отправки HTTP-запросов
from bs4 import BeautifulSoup  # Для парсинга HTML и XML документов
import urllib.parse  # Для склейки URL
from datetime import datetime  # Для работы с датами и временем
import time  # Для работы со временем
import re  # Для работы с регулярными выражениями
import json  # Для работы с форматом данных JSON


# Функция для получения данных о кассовых сборах
def get_box_office_data():
    # URL страницы, с которой будут собираться данные
    url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'
    # Заголовки запроса для имитации запроса от браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

    # Отправка GET-запроса на URL
    response = requests.get(url, headers=headers)
    # Разбор HTML-кода страницы
    soup = BeautifulSoup(response.content, 'html.parser')

    # Список для хранения ссылок на страницы с детальной информацией о фильмах
    release_links = []
    # Поиск всех элементов td с определенным классом, содержащих ссылки на фильмы
    for link in soup.find_all('td', class_='a-text-left mojo-field-type-release mojo-cell-wide'):
        a_tag = link.find('a')  # Поиск тега <a> внутри элемента
        if a_tag:
            release_links.append(a_tag.get('href'))  # Добавление ссылки на фильм в список

    # Преобразование относительных ссылок в абсолютные
    url_joined = [urllib.parse.urljoin('https://www.boxofficemojo.com', link) for link in release_links]

    # Список для хранения собранных данных
    data = []
    # Перебор всех ссылок для получения детальной информации о каждом фильме
    for url in url_joined:
        response = requests.get(url, headers=headers)  # Отправка запроса
        soup = BeautifulSoup(response.content, 'html.parser')  # Разбор HTML
        # Поиск таблицы с основной информацией о фильме
        table = soup.find('div', class_='a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile')
        print("1")
        if not table:
            continue

        # Сбор данных из таблицы
        rows = table.find_all('div', class_='a-section a-spacing-none')

        row_data = {}  # Словарь для хранения данных о фильме
        for row in rows:
            key = row.find('span').text.strip()  # Ключ (название поля)
            spans = row.find_all('span')
            if len(spans) > 1:
                value = spans[1].text.strip()  # Значение поля
                # Преобразование данных в соответствии с их типом
                if key == 'Opening':
                    value = int(re.sub('[^0-9]', '', value))  # Преобразование строки в число
                elif key == 'Release Date':
                    value = value  # Дата без изменений
                elif key == 'Running Time':
                    try:
                        time_parts = re.findall(r'\d+', value)  # Разбиение времени на части
                        hours, minutes = map(int, time_parts)  # Преобразование в часы и минуты
                        value = hours * 3600 + minutes * 60  # Перевод в секунды
                    except ValueError:
                        continue
                elif key == 'Genres':
                    value = [genre.strip() for genre in value.split(',') if genre.strip()]  # Разбиение жанров на список
                elif key == 'In Release':
                    value = re.sub(r'[^\d]', '', value)  # Удаление нечисловых символов
                elif key == 'Widest Release':
                    value = int(re.sub('[^0-9]', '', value))  # Преобразование строки в число

                row_data[key] = value  # Добавление пары ключ-значение в словарь

        if row_data:
            data.append(row_data)  # Добавление данных о фильме в общий список
        time.sleep(1)  # Задержка для предотвращения блокировки (закомментировано)

    return data  # Возврат собранных данных


# Функция для сохранения данных в формате JSON
def save_data_to_json(data, filename='box_office_data.json'):
    with open(filename, 'w') as f:  # Открытие файла для записи
        json.dump(data, f, indent=4)  # Сохранение данных в формате JSON с отступами


# Главная функция
def main():
    data = get_box_office_data()  # Получение данных о кассовых сборах
    save_data_to_json(data)  # Сохранение данных в файл


if __name__ == "__main__":
    main()
