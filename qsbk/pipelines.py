# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class QsbkPipeline(object):

    def __init__(self):
        self.fp = open("2.txt", "a+", encoding='utf-8')
        self.fp2 = open("段子.json", 'w', encoding='utf-8')

    def open_spider(self, spider):
        print("爬虫开始了")
        print("你哈")

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp2.write(item_json + '\n')
        # return item

    def close_spider(self, spider):
        self.fp.close()
        self.fp2.close()
        print("爬虫结束了")

# 数据多是比较占内存，它是把所有数据存入列表，最后再写入
# from  scrapy.exporters import JsonItemExporter
# class QsbkPipeline(object):
#
#     def __init__(self):
#         self.fp2=open("duanzi.json",'wb')
#         # self.exporter=JsonItemExporter(self.fp2,ensure_asscii=False,encoding='utf-8')
#         self.exporter=JsonItemExporter(self.fp2,encoding='utf-8')
#         self.exporter.start_exporting()
#
#
#     def open_spider(self,spider):
#         print("爬虫开始了")
#
#     def process_item(self, item, spider):
#
#         self.exporter.export_item(item)
#         return item
#
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp2.close()
#         print("爬虫结束了")


# 数据多采用这方法，数据是以行为单位写入的
# from scrapy.exporters import JsonLinesItemExporter
# class QsbkPipeline(object):
#
#     def __init__(self):
#         self.fp2=open("duanzi.json",'wb')
#         # self.exporter=JsonItemExporter(self.fp2,ensure_asscii=False,encoding='utf-8')
#         self.exporter=JsonLinesItemExporter(self.fp2,encoding='utf-8')
#         self.exporter.start_exporting()
#
#
#     def open_spider(self,spider):
#         print("爬虫开始了")
#
#     def process_item(self, item, spider):
#
#         self.exporter.export_item(item)
#         return item
#
#
#     def close_spider(self,spider):
#
#         self.fp2.close()
#         print("爬虫结束了")
