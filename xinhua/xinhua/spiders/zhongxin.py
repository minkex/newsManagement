# -*- coding: utf-8 -*-
import scrapy
import re
import time
import requests
from scrapy import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup
from xinhua.items import XinhuaItem
from xinhua.logs import logtools
from xinhua.tool.filterurl import isMpage
from xinhua.tool.parsepage import parsePage
from xinhua.config.config import website_info
from xinhua.tool.filterurl import filter_invalid_urls
from scrapy.shell import inspect_response

class ZhongxinSpider(scrapy.Spider):
    name = 'zhongxin'
    start_urls = []
    urllieb =website_info.zhongxinURLS
    def start_requests(self):
        for zhongxinURL in self.urllieb:
            logtools.write_err('yunxingle')
            yield Request(zhongxinURL,callback=self.parse_list)
    '''def parse(self,response):
        start_url=response.urljoin(self.start_urls[0])
        self.urllieb.append(start_url)
        for page in self.urllieb:
            url = response.urljoin(page)
            logtools.write_err('yunxingle')
            yield Request(url, callback=self.parse_list)'''
    def parse_list(self, response):

        res_url = response.url
        logtools.write_err(res_url)
        logtools.write_info('------------------')
        ctype, url_type = isMpage(res_url)
        if ctype:
            yield self.parse_page(response, ctype, url_type)
        elif re.match(r'http://www.chinanews.com/scroll-news.*',res_url):
            logtools.write_err(u'............解析')
            urls = Selector(response).xpath('//a/@href').extract()
            Urls=[]

            for url in urls:
                u=response.urljoin(url)
                Urls.append(u)
            vaild_urls = filter_invalid_urls(Urls)
            for url in vaild_urls:
                yield Request(url,callback=self.parse_list)

    def parse_page(self,response,ctype,url_type):
        item = XinhuaItem()
        urls = response.url
        item['url'] = urls
        item['html_code'] = response.body
        hsel = Selector(response)
        item['encoding'] = 'utf-8'
        item['ctype'] = ctype
        item['subtype'] = url_type
        logtools.write_info(u'开始爬取' + urls)
        parsePage(item, hsel, url_type,urls)
        item['originality'] = item['source']
        item['copyright'] = item['source']
        item['type1'] = 'text'
        item['crawltime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        logtools.write_info(urls + u'爬取结束')
        return item
