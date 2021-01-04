# Crawl 250 Best Movies from IMDB

[![Python Version](https://img.shields.io/badge/python-3.8.5-brightgreen.svg)](https://python.org)
[![Scrapy Version](https://img.shields.io/badge/scrapy-2.4.1-brightgreen.svg)](https://scrapy.org)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/rdmaulana/scrapy-imbd.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Set up your Postgresql database by edit pipelines.py:
```bash
hostname = 'YOUR_HOST'
username = 'YOUR_DB_USERNAME'
password = 'YOUR_DB_PASSWORD'
database = 'YOUR_DB_NAME'
```

Finally, run scrapy:

```bash
scrapy crawl best_movies
```

If want to put some json output:

```bash
scrapy crawl best_movies -o result.json
```



