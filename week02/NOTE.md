学习笔记
1、open函数中，a与a+的区别，a只用于追加，a+还可以用于读文件。都是用来追加内容
2、scrapy框架的pipeline中可以重写open_spider和close_spider两个方法，用来打开和关闭的操作，并且只在爬虫开始和关闭时执行
用法1：文件读写
class JsonWritePipeline:
	def open_spider(self, spider):
		self.file = open(‘items.jl’, ‘w’)
	def process_item(self, item, spider):
		line = json.dump(dict) + “\n”
		self.flie.write(line)
		return item
	def close_spider(self, spider):
		self.file.close()
用法2：数据库连接和关闭
class mysqlPipeline(object):
    conn = None
    def open_spider(self, spider):
        self.conn =pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db=’test’)
    def proccess_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into table values("s%","s%")'%(item["author"],item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self, spider):
        #self.cursor.close()
        self.conn.close()
3、os模块中path的使用，返回上一层目录os.path.dirname(__file__),返回绝对路径os.path.abspath(__file__)
	