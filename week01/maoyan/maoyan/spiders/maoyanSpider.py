from time import sleep

import scrapy

from maoyan.items import MaoyanItem


class MaoyanspiderSpider(scrapy.Spider):
    name = 'maoyanSpider'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    #取出前10部电影的url
    def parse(self, response):
        re = response.xpath('//dl//div[@class="movie-item film-channel"]')
        for urls in re:
            item = MaoyanItem()
            url = 'https://maoyan.com' + urls.xpath('./a/@href')[0:10].extract_first()
            yield scrapy.Request(url=url,callback=self.parse2)
            sleep(2)
    #解析电影名称、类型、上映时间
    def parse2(self, response):
        re1 = response.xpath('//div[@class="movie-brief-container"]')
        for movie in re1:
                item = MaoyanItem()
                item['title'] = movie.xpatn('./h1/text()').extract_first()
                item['film_type'] = movie.xpatn('./ul/li[1]/a[1]/text()').extract_first()
                item['film_date'] = movie.xpatn('./ul/li[3]/text()').extract_first()
                yield item

