# PEP Parser

## Описание

PEP Parser — это Scrapy-парсер для сбора информации о Python Enhancement Proposals с официального сайта [peps.python.org](https://peps.python.org/).

Парсер собирает данные о PEP-документах:

* номер PEP;
* название PEP;
* статус PEP.

Также проект формирует сводный CSV-файл с количеством PEP по каждому статусу.

## Технологии

* Python
* Scrapy

## Установка и запуск проекта

Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone https://github.com/YuliiaProshina/scrapy_parser_pep.git
cd scrapy_parser_pep
```

Создайте и активируйте виртуальное окружение.

```bash
python -m venv venv
source venv/Scripts/activate
```

Обновите pip:

```bash
python -m pip install --upgrade pip
```

Установите зависимости:

```bash
python -m pip install -r requirements.txt
```

## Запуск парсера

Для запуска парсера выполните команду:

```bash
scrapy crawl pep
```

## Результаты работы

После запуска парсера в директории `results/` создаются два CSV-файла:

```text
pep_<дата_и_время>.csv
status_summary_<дата_и_время>.csv
```

Файл `pep_<дата_и_время>.csv` содержит список всех найденных PEP:

```text
number,name,status
1,PEP Purpose and Guidelines,Active
...
```

Файл `status_summary_<дата_и_время>.csv` содержит сводку по статусам:

```text
Статус,Количество
Active,31
Final,276
...
Total,600
```

## Структура проекта

```text
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   └── pep.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── items.py
│   ├── pipelines.py
│   └── settings.py
├── results/
├── tests/
├── requirements.txt
├── scrapy.cfg
└── README.md
```



## Проверка кода

Для проверки стиля кода можно использовать Flake8:

```bash
python -m flake8 pep_parse
```


## Автор

Прошина Юлия — студент Яндекс.Практикума  
[LinkedIn](https://www.linkedin.com/in/yuliia-proshina-160551372)