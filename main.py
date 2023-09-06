import sqlite3


# Функция для создания регулярных выражений на основе доменов
def create_regex(domains):
    # Создаем список уникальных поддоменов
    subdomains = set()
    for domain in domains:
        subdomain = domain.split('.', 1)[0]
        subdomains.add(subdomain)

    # Формируем регулярное выражение
    regex = '^(' + '|'.join(subdomains) + ')'

    return regex


# Подключение к базе данных
conn = sqlite3.connect('domains.db')
cursor = conn.cursor()

# Получение всех уникальных project_id из таблицы domains
cursor.execute('SELECT DISTINCT project_id FROM domains')
project_ids = cursor.fetchall()

# Для каждого project_id создаем регулярное выражение и записываем его в таблицу rules
for p_id in project_ids:
    cursor.execute('SELECT name FROM domains WHERE project_id=?', p_id)
    results = cursor.fetchall()

    # Преобразуем список кортежей в список значений
    domains = [result[0] for result in results]

    regex = create_regex(domains)
    cursor.execute('INSERT INTO rules (regexp, project_id) VALUES (?, ?)', (regex, p_id[0]))

# Удаляем дублирующиеся записи
cursor.execute('DELETE FROM rules WHERE rowid NOT IN (SELECT MIN(rowid) FROM rules GROUP BY project_id)')

# Сохранение изменений в базе данных
conn.commit()

# Закрытие соединения с базой данных
conn.close()