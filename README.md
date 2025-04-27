# lighting-spider
# Парсер источников освещения с Divan.ru (отдельный репозиторий)

[![Scrapy](https://img.shields.io/badge/Scrapy-2.11+-blue.svg)](https://scrapy.org/)

Парсер для сбора данных о товарах категории "Свет" с сайта divan.ru. Экспортирует данные в CSV-файл.

## 📋 Особенности
- Сбор названия, цены и ссылки на товар
- Автоматическая обработка пагинации
- Защита от блокировки:
  - Задержка между запросами: 1 сек
  - Ограничение параллельных потоков: 2
  - Кастомные User-Agent
- Экспорт в CSV с заданным порядком колонок

## ⚙️ Требования
- Python 3.13
- Scrapy 2.11+

## 🛠 Установка
```bash
git clone https://github.com/JohnDroben/lighting-spider.git
cd lighting-spider
pip install -r requirements.txt


## 🚀 Запуск
bash
scrapy crawl divannewpars -O output.csv
Пример данных:
________________________________________
csv
name,price,link
"Люстра Crystal",15990,https://divan.ru/product/123
"Торшер Modern",8900,https://divan.ru/product/456
_________________________________________________
 ## Важно
Обновите CSS-селекторы при изменении структуры сайта
Не превышайте 10 запросов в минуту
