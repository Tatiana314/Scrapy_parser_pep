# Проект парсинга документов PEP на базе фреймворка Scrapy.

Программа осуществляет сбор информации о PEP (Python Enhancement Proposals): номер РЕР, название, статус. Реализован подсчет количества в каждом статусе и общее количество PEP.

Для запуска проекта необходимо выполнить следующую команду:
```
'scrapy crawl pep'
```
После выполнения команды, парсер начнет сбор информации о PEP с официального сайта Python - https://peps.python.org/. Полученные данные сохраняются в директорию results в формате csv-файла.

## Технологии
Python3, Scrapy. 

## Запуск проекта
Клонировать репозиторий:
```
git clone https://github.com/Tatiana314/Scrapy_parser_pep.git
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

## Автор
[Мусатова Татьяна](https://github.com/Tatiana314)
