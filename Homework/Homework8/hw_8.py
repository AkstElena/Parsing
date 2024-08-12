import pandas as pd  # для обработки и анализа данных
import numpy as np  # библиотека для работы с массивами данных
import matplotlib.pyplot as plt  # модуль для построения графиков
import seaborn as sns  # библиотека для визуализации данных, основанная на matplotlib
from sklearn.preprocessing import \
    LabelEncoder  # инструмент для кодирования категориальных переменных (уходим от символов к числам)
from scipy import stats  # библиотека для научных и математических вычисление

# установка стиля и цветовой палитры для графиков
sns.set(style='whitegrid')

# загрузка данных
file_path = 'train.csv'
df = pd.read_csv(file_path)

# вывод датасета
print('Общая информация:')
print(df.info())

# Setting value of columns=80
pd.set_option('display.max_columns', 80)

# print('Первые строки датасета:')
# print(df.head())

# print('\n статистика:')
# print(df.describe())
#

# Проверка того, в каких столбцах отсутствуют значения
print(df.isnull().sum())
# # обработка отстуствующих значений
# # Всем пропущенным цифровым данным присвоены значения
# numeric_cols = df.select_dtypes(include=[np.number])  # выбор числовых колонок
# df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())  # замена пропущенных значений на среднее
# # print(df[numeric_cols.columns])
#
# categorical_cols = df.select_dtypes(include=['object'])  # выбор категориальных колонок
# df[categorical_cols.columns] = categorical_cols.fillna(
#     categorical_cols.mode().iloc[0])  # замена пропущенных значений на моду (самое встречаемое)
# # print(df[categorical_cols.columns])
#
# # удаление дублирующих строк
# df.drop_duplicates(inplace=True)
#
# # гистограмма распределения рейтингов
# # plt.figure(figsize=(10, 6))  # размер поля графика
# # sns.histplot(df['Rating'], kde=True, color='skyblue')  # построение гистограммы и кривой плотности распределения
# # plt.title('Distr of App rating')
# # plt.show()  # отображение графика
#
# # распределение приложений по категориям
# # plt.figure(figsize=(12, 8))  # размер поля графика
# # sns.countplot(y='Category', data=df, order=df['Category'].value_counts().index, palette='viridis')
# # plt.title('App Distr across Categories')
# # plt.show()  # отображение графика
#
# # распределение платных и бесплатных приложений
# # plt.figure(figsize=(7, 5))
# # sns.countplot(x='Type', data=df)
# # plt.title('Free vs Paid')
# # plt.show()  # отображение графика
#
# # Обнаружение и обработка выбросов
# z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number)))  # z оценка для числовых переменных
# df = df[(z_scores < 3).all(axis=1)]  # удаление строк с выбросами
# # эта строка выполняет фильтрацию строк в DataFrame на основе условия, связанного с Z-оценками (z-scores)
#
# # стандартизация данных (числовых переменных)
# df_standardized = df.copy()
# df_standardized[numeric_cols.columns] = (df_standardized[numeric_cols.columns] - df_standardized[
#     numeric_cols.columns].mean()) / df_standardized[numeric_cols.columns].std()
#
# # Создание доп столбца
# label_encoder = LabelEncoder()
# df['Type_Encoded'] = label_encoder.fit_transform(df['Type'])  # преобразование категорийной переменной в числовую, то есть где  Free  станет 0, а где платно 1
#
#
# output_file_path = 'clear_gapps_lE.csv'
# df.to_csv(output_file_path, index=False)
#
# # df = pd.get_dummies(df, columns=['Content Rating'], prefix='ContentRating', drop_first=True)
# #
# # # Создание сводной таблицы
# # pivot_table = df.pivot_table(index='Category', columns='ContentRating_Teen', values='Rating', aggfunc='mean')
# # print('\n Сводная таблица: ')
# # print(pivot_table)
#
# # Сохранение
# # output_file_path = 'clear_gapps.csv'
# # df.to_csv(output_file_path, index=False)

