# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
    将爬取的数据存入数据库中
'''
import pymysql
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        #链接数据库
        db = pymysql.connect('localhost','root','123456','market')
        print(db)
        #获取cur操作游标对象
        cur = db.cursor()
        #获取电影排名
        movie_rank = item['rank'][0]
        #获取电影名称
        movie_title = item['name'][0]
        sql = 'insert into douba values(null,%s,%s)'
        #发送SQL语句，并设置参数
        cur.execute(sql,((movie_rank),(movie_title)))
        db.commit()
        return item
