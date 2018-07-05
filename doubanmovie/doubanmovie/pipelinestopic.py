# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
    在控制端输出文本信息
'''
#导入os模块
import os
import urllib
class DoubanmoviePipeline(object):
    #构造方法
    def __init__(self):
        #创建文件夹名称
        self.folder_name = 'douban_output/image'
        #判断文件夹是否存在
        if not os.path.exists(self.folder_name):
            #若文件夹不存在，则创建
            os.mkdir(self.folder_name)
            pass
        pass
    #处理每一个采集到的数据
    def process_item(self, item, spider):
        print('--->图片采集：下载图片保存在本地')
        #获取电影详情链接
        movie_pic = item['pic'][0]
        #拆分字符串，并获取最后一个元素作为图片名称
        image_name = movie_pic.split('/')[-1]
        try:
            #下载图片保存到指定的文件夹中
            urllib.request.urlretrieve(movie_pic, self.folder_name +'/%s' %image_name)
            pass
        except:
            print('文件操作失败')
        return item
