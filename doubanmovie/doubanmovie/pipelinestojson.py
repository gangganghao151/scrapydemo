# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
    在控制端输出文本信息
'''
from __future__ import unicode_literals
import time
import os
import json
import codecs
import sys
#定义一个全局的list变量
json_list = []

class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        #创建输出文件夹
        folder_name = 'douban_output'
        #获取系统时间
        current_time = time.strftime('%Y-%m-%d',time.localtime())
        #设置文件保存名称
        file_name = 'doubanmovietop20'+current_time+'.json'
        try:
            with codecs.open(folder_name+os.sep+file_name,'a') as fp:
                #将读取到的每一行电影信息转换成json格式
                line = json.dumps(json_list,ensure_ascii=False)+'\n'
                #向文件写入
                fp.write(line)
                print('文件写入成功')
                pass
            pass
        except:
            print('文件操作失败')
            pass
        return item
