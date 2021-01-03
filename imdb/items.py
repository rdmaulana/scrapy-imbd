# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    title = scrapy.Field()
    realease = scrapy.Field()
    rating = scrapy.Field()
    genre = scrapy.Field()
    duration = scrapy.Field()
    url = scrapy.Field()
