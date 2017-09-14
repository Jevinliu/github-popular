# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook
from scrapy.conf import settings
import pymongo


class PopularPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']  # 数据库名
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbname]
        self.post = tdb[settings['MONGODB_DOCNAME']]  # 表名

    def process_item(self, item, spider):
        agentinfo = dict(item)
        self.post.insert(agentinfo)
        return item
