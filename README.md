# Scrapy_parser_pep - проект парсинга документов PEP на базе фреймворка Scrapy.
Парсер собирает ссылки на документы PEP со стартовой страницы по адресу https://peps.python.org/ и переходит по каждой ссылке, чтобы получить актуальную информацию о каждом документе PEP.
Парсер работает в асинхронном режиме, что существенно ускоряет процесс парсинга. После сбора информации, парсер обрабатывает ее и выводит результаты в два файлы формата .csv. Названия файлов содержат временную метку для уникальности.
В первом файле выводится список всех PEP документов вместе с их номерами, названиями и статусами. Во втором файле представлена сводка по статусам PEP - количество документов, найденных в каждом статусе. В последней строке второго файла указана общая информация о количестве всех найденных документов.
Файлы сохраняются в папку results, находящуюся в корне проекта.

## Технологии
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?logo=Scrapy)](https://docs.scrapy.org/en/latest/)
[![CSS](https://img.shields.io/badge/-CSS_selectors-464646?logo=CSS)](https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors)
[![XPath](https://img.shields.io/badge/-XPath_selectors-464646?logo=XPath)](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)

## Запуск проекта
Клонировать репозиторий:
```
git clone https://github.com/Tatiana314/Scrapy_parser_pep.git && cd Scrapy_parser_pep
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
Linux/macOS: source env/bin/activate
windows: source env/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Запустить приложение:
```
scrapy crawl pep
```

## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)
