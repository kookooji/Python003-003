# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):

    title = scrapy.Field()
    film_date = scrapy.Field()
    film_type = scrapy.Field()
