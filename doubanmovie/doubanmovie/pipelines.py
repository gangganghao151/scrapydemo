# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
    在控制端输出文本信息
'''

class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        print('电影排名：{0}'.format(item['rank'][0]),end='>>>>')
        print('电影名称：{0}'.format(item['name'][0]))
        return item
