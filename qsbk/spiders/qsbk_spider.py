# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from qsbk.items import QsbkItem
# 安装pywin32
#安装cffi(出错删除重装)
# 在命令行输入 scrapy startproject+项目名创建项目
# cd 项目名
# scrapy genspider 类名 +"url地址"
# 使用scrapy crawl +项目名运行项目
class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/text/page/1']
    basicurl="http://qiushibaike.com"

    def parse(self, response):
        # print("asda")
        # print(type(response))
        a=response.xpath("//div[@class='col1 old-style-col1']/div")
        for i in a:
            b=i.xpath(".//h2/text()").get()
            context=i.xpath(".//div[@class='content']//text()").getall()
            # print(b)
            context="".join(context).strip()
            item=QsbkItem(author=b,content=context)
            print(item)
            # yield  item
        nexturl=response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not nexturl:
            return
        else:
            yield scrapy.Request(self.basicurl+nexturl,callback=self.parse)
        pass
