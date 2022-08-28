# Scrapy-Spiders
Collection of Scrapy Spiders

## Prerequisites
```bash
pip install scrapy
```
or
```bash
conda install scrapy
```
## Quote Spider to json
```bash
scrapy runspider quotes_spider.py -o quotes.json
```
## NFL Schedule Spider (2008-2018) to csv
```bash
scrapy runspider nfl_schedule_spider.py -o nfl_schedule.csv
```
## NFL News Spider to csv
```bash
scrapy runspider nfl_news_spider.py -o nfl_news.csv
```
## CTA to json
```bash
scrapy runspider cta_spider.py -o cta.json
```