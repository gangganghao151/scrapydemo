# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
    输出信息到excel中
'''
#导入模块
import time
import os
import xlrd,xlwt
#导入xlutils中的copy模块
from xlutils.copy import copy
class DoubanmoviePipeline(object):

    #构造函数，创建一个excel表格
    def __init__(self):
        #创建输出文件夹的名字
        folder_name = 'douban_output'
        #获取当前系统时间
        current_time = time.strftime('%Y-%m-%d',time.localtime())
        #设置保存文件名
        file_name = 'doubanmovietop20'+current_time+'.xls'
        #文件的最终路径
        self.excelPath = folder_name+os.sep+file_name
        #创建一个工作簿
        self.wb = xlwt.Workbook(encoding='utf-8')
        #创建sheet页
        self.sheet = self.wb.add_sheet('豆瓣电影信息')
        #设置Excel标题栏内容
        headers = ['电影排名','电影名称','图片链接']
        #循环写入标题内容
        for colIndex in range(0,len(headers)):
            self.sheet.write(0,colIndex,headers[colIndex])
            pass
        #保存创建好的文件
        self.wb.save(self.excelPath)
        #设置excel行全局变量
        self.rowIndex= 1
        pass
    def process_item(self, item, spider):
        #打开已经存在的excel
        oldwb = xlrd.open_workbook(self.excelPath,formatting_info=True)
        #拷贝一个副本
        newwb = copy(oldwb)
        #从excel中获取第一页
        sheet = newwb.get_sheet(0)
        #将采集的数据转化为一个list
        line =  [item['rank'],item['name'],item['pic']]
        #循环追加写入
        for colIndex in range(0,len(item)):
            sheet.write(self.rowIndex,colIndex,line[colIndex])
            pass
        #自动覆盖原有文件
        newwb.save(self.excelPath)
        self.rowIndex=self.rowIndex+1
        print('文件写入完毕')
        return item
