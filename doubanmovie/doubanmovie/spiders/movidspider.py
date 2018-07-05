# -*- coding: utf-8 -*-
import scrapy

#导入类
from doubanmovie.items import DoubanmovieItem
class MovidspiderSpider(scrapy.Spider):
    name = 'movidspider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_item = response.xpath('//div[@class="item"]')
        for item in movie_item:
            #创建一个movie对象
            movie = DoubanmovieItem()
            movie['rank'] = item.xpath('div[@class="pic"]/em/text()').extract() #提取文本内容
            movie['name'] = item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            movie['pic'] = item.xpath('div[@class="pic"]/a/img/@src').extract()
            yield movie
            pass
        pass
