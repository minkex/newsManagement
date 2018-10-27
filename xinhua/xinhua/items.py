# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinhuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()                        #页面链接
    html_code = scrapy.Field()                  #HTML源码
    encoding = scrapy.Field()                   #页面编码
    title = scrapy.Field()                      #标题
    authors=scrapy.Field()                      #作者
    content=scrapy.Field()                      #正文
    time=scrapy.Field()                         #新闻时间
    source=scrapy.Field()                       #来源
    editor=scrapy.Field()                       #编辑
    ctype = scrapy.Field()                      #频道类别
    subtype = scrapy.Field()                    #频道类别英文
    keywords=scrapy.Field()                     #关键词
    abstract=scrapy.Field()                     #摘要
    crawltime=scrapy.Field()                    #爬取时间
    copyright=scrapy.Field()                    #版权
    originality=scrapy.Field()                  #来源
    type1=scrapy.Field()                        #类别
    img=scrapy.Field()                          #图片

