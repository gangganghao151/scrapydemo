#-*- coding:utf-8 -*-
'''
    demo01.py
    ======================
    @author xxx
    @date 2018-7-1
    
'''
from scrapy import cmdline
if __name__=='__main__':
    cmdline.execute('scrapy crawl movidspider'.split())
    pass