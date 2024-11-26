#імпорт бібліотек.
import pandas as pd
import matplotlib.pyplot as plt

#налаштування стилю графіку.
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 10)

#завантаження даних з CSV-файлу.
file_path = 'data_2010.csv'
df = pd.read_csv(file_path, sep=',', encoding='latin1',
                 parse_dates=[0],  #перша колонка (індекс 0) - це дати.
                 dayfirst=True,
                 index_col=0,  #використовуємо першу колонку як індекс.
                 header=0,  #перша строка є заголовком.
                 names=['Date', 'Time', 'Rachel / Papineau', 'Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brébeuf', 'Parc', 'CSC (Côte Sainte-Catherine)', 'PierDup'])

#видалення порожньої колонки (якщо вона є).
df = df.dropna(axis=1, how='all')

#виведення перших кількох рядків датафрейму для перевірки.
print("Перші кілька рядків датафрейму:")
print(df.head(3))

#додавання нового стовпця з номером місяця.
df['Month'] = df.index.month

#вибір лише числових стовпців для аналізу.
numeric_columns = df.select_dtypes(include=['number'])

#обчислення сумарного відвідування за місяцями.
monthly_data = numeric_columns.groupby(df['Month']).sum()

#знаходимо місяць із найбільшою кількістю відвідувань.
most_popular_month = monthly_data.sum(axis=1).idxmax()
print(f"Найбільш популярний місяць у велосипедистів: {most_popular_month}")

#побудова графіку відвідуваності велодоріжок.
numeric_columns.drop(['Month'], axis=1).plot(figsize=(15, 10), title="Використання велодоріжок у 2010 році")
plt.xlabel("Дата")
plt.ylabel("Кількість відвідувань")
plt.show()
