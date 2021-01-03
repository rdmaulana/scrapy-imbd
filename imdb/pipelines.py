# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class ImdbPipeline:
    def open_spider(self, spider):
        hostname = 'YOUR_HOST'
        username = 'YOUR_DB_USERNAME'
        password = 'YOUR_DB_PASSWORD'
        database = 'YOUR_DB_NAME'
        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            dbname=database
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute(
            "INSERT INTO best_movie(title, realease, rating, genre, duration, url)\
            VALUES(%s,%s,%s,%s,%s,%s)",
            (
                item['title'],
                item['realease'],
                item['rating'],
                item['genre'],
                item['duration'],
                item['url']
            ) 
        )
        self.connection.commit()
        return item
