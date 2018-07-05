# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
    在文本文件中输出文本信息
'''
#导入os模块
import  os
import time
class DoubanmoviePipeline(object):
    #构造函数--------做初始化操作
    def __init__(self):
    #创建文件夹名称
        self.folder_name = 'douban_output'
        if not os.path.exists(self.folder_name):
            #创建目录
            os.mkdir(self.folder_name)
        pass
    """
    处理采集到的每一个电影信息
    """
    def process_item(self, item, spider):
        print('--->TXT:write to text file……')
        #获取当前系统时间
        current_date = time.strftime('%Y-%m-%d',time.localtime())
        #设置保存文件的名称
        file_name = 'doubanmovietop20'+current_date+'.txt'
        try:
            with open(self.folder_name+os.sep+file_name,'a',encoding='utf8') as fp:
                #写入相关数据
                fp.write('电影排名：{0}\t\t电影名称：{1}\t\t\n'.format(item['rank'][0],item['name'][0]))
                pass
            pass
        except:
            print('文件写入出错')
            pass
        return item
