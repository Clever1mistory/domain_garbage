# Описание

Это тестовое задание. Задание состоит в создании скрипта на Python для фильтрации "мусорных" доменов на основе предоставленной базы данных SQLite.

Скрипт считывает данные из базы данных и для каждого уникального project_id создает регулярное выражение. Регулярные выражения записываются в таблицу rules. Эти регулярные выражения будут использоваться для фильтрации доменов и отсеивания "мусорных" доменов.

# Требования

- Python 3.x
- Модуль sqlite3

# Установка и настройка

1. Скачайте код с репозитория или склонируйте репозиторий.
2. Установите зависимости, включая модуль sqlite3, при помощи pip:
```
pip install sqlite3
```
3. Загрузите базу данных SQLite, предоставленную в задании.

# Использование

1. Запустите скрипт main.py:
```
python main.py
```
Скрипт подключится к базе данных, считает данные, создаст регулярные выражения и запишет их в таблицу rules.

2. После успешного выполнения скрипта, таблица rules будет содержать регулярные выражения, связанные с каждым project_id.(В репозитории находится уже готовая БД)

# Дополнительные замечания

- Функция create_regex может быть настроена для создания более сложных и точных регулярных выражений в зависимости от требований и конкретики задачи фильтрации доменов.