# scrapy-imbd
Crawling Best 250 Movies.

Storing in Database PostgreSQL.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/rdmaulana/scrapy-imbd.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Finally, run scrapy:

```bash
scrapy crawl best_movies
```

If want to put some json output:

```bash
scrapy crawl best_movies -o result.json
```



