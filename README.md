<a name="Начало"></a>

## Product Parser

![Product Parser](https://github.com/dmsnback/product_parser/actions/workflows/main.yml/badge.svg) ![Python](https://img.shields.io/badge/python-3.11-blue) ![Black](https://img.shields.io/badge/code%20style-black-000000) ![License](https://img.shields.io/badge/license-MIT-green)


- [Описание](#Описание)
- [Технологии](#Технологии)
- [Запуск проекта](#Запуск)
- [Формат выходных данных](#Формат)
- [Автор](#Автор)

<a name="Описание"></a>

### Описание

Парсер интернет-магазина [alkoteka.com](alkoteka.com "Перейти"), написанный на Scrapy.
Собирает товары из заданных категорий с учётом региона (Краснодар) и сохраняет данные в формате JSON по заданному шаблону.

> [Вернуться в начало](#Начало)

<a name="Технологии"></a>

### Технологии

[![Python](https://img.shields.io/badge/Python-1000?style=for-the-badge&logo=python&logoColor=ffffff&labelColor=000000&color=000000)](https://www.python.org)
[![Scrapy](https://img.shields.io/badge/Scrapy-1000?style=for-the-badge&logo=scrapy&logoColor=ffffff&labelColor=000000&color=000000)](https://docs.scrapy.org/en/latest/index.html)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=ffffff&labelColor=000000&color=000000)](https://github.com/features/actions)

> [Вернуться в начало](#Начало)

<a name="Запуск"></a>

### Запуск проекта

- Склонируйте репозиторий

```python
git clone git@github.com:dmsnback/product_parser.git
```

- Установите и активируйте виртуальное окружение

```python
python3 -m venv venv
```

Для `Windows`

```python
source venv/Scripts/activate
```

Для `Mac/Linux`

```python
source venv/bin/activate
```

- Установите зависимости из файла
`requirements.txt`

```python
python3 -m pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

- Запускаем парсер

```python
crapy crawl alkoteka_catalog -O result.json        
```

- После завершения работы парсера появится файл ```result.json```

> [Вернуться в начало](#Начало)

<a name="Формат"></a>

### Формат выходных данных

```json
{
    "timestamp": 1772382781,
    "RPC": "77235",
    "url": "https://alkoteka.com/product/vino-tikhoe/golubickoe-esteyt-shardone_77235",
    "title": "Голубицкое Эстейт Шардоне, 0.75 Л, Белое",
    "marketing_tags": ["Скидка"],
    "brand": "Поместье Голубицкое",
    "section": "Вино тихое",
    "price_data": {
        "current": 1130.0,
        "original": 949.0,
        "sale_tag": "Скидка 16%"},
    "stock": {
        "in_stock": true,
        "count": 7107},
    "assets": {
        "main_image": "https://web.alkoteka.com/storage/product/7b/53/77235_image.png",
        "set_images": [],
        "view360": [],
        "video": []},
    "metadata": {
        "__description": "Цвет светло-соломенный  Аромат яркий, с оттенками белых цветов, тропических фруктов и ванили  Вкус сбалансированный, с нотами дыни, жёлтой груши, манго, ананаса, луговых цветов и лёгкими цитрусовыми нюансами в послевкусии",
        "Артикул": "77235",
        "Страна производитель": "Россия",
        "Производитель": "Поместье Голубицкое",
        "Цвет": "Белое",
        "Объём": "min-0.75л., max-0.75л.",
        "Крепость": "min-12.5%, max-12.5%"},
        "variants": 1
}
```

> [Вернуться в начало](#Начало)

<a name="Автор"></a>

### Автор

- [Титенков Дмитрий](https://github.com/dmsnback)

> [Вернуться в начало](#Начало)
