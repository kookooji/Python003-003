# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanPipeline:
    def open_spider(self,spider):
        print('p爬虫开始')

    def process_item(self, item, spider):
        title = item['title']
        film_type = item['film_type']
        film_date = item['film_date']
        output = f'|{title}|\t|{film_type}|\t|{film_date}|\n\n'
        with open('./maoyanmovie.csv', 'a', encoding='utf-8') as f:
            f.write(output)
        return item

    def close_spider(self,spider):
        print('爬虫结束')

#将数据保存到数据库
class mysqlPipeline(object):
    conn = None
    def open_spider(self, spider):
        self.conn =pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='movies')
    def proccess_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into maoyan values("s%","s%","s%")'%(item["title"],item["flim_type"],item['flim_date']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()