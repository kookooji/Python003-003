# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        title = item['title']
        film_type = item['film_type']
        film_date = item['film_date']
        output = f'|{title}|\t|{film_type}|\t|{film_date}|\n\n'
        with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as f:
            f.write(output)
        return item
