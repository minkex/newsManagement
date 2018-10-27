# -*- coding: utf-8 -*-
import scrapy
import time
import json
import re
import requests
from bs4 import BeautifulSoup
from scrapy import Selector
from xinhua.logs import logtools
from xinhua.tool.filterurl import isMpage
from xinhua.items import XinhuaItem
from xinhua.tool.parsepage import parsePage

from xinhua.tool.filterurl import filter_invalid_urls
from scrapy.http import Request
from xinhua.config.config import website_info
from scrapy.shell import inspect_response
class XinhuatestSpider(scrapy.Spider):
    name = 'xinhuaTest'
    start_urls = ['http://qc.wa.news.cn/nodeart/list?nid=113352&pgnum=1&cnt=10&tp=1&orderby=1?']
    urllieb=website_info().get_URLs()
    def parse(self, response):
        logtools.write_info(u'............开始解析............' )
        first_sel=Selector(response)
        res_url=response.url
        logtools.write_info('------------------')
        logtools.write_info(u'............开始解析............'+res_url)
        ctype,url_type=isMpage(res_url)
        if ctype:
            logtools.write_err(u'............开始解析动态............' + res_url)
            yield self.parse_page(response,ctype,url_type)
        elif re.match(r'http://qc.wa.news.cn/nodeart/list.*',res_url):
            logtools.write_info(u'............开始解析动态............' )
            for j in range(0,len(self.urllieb)):
                logtools.write_err(u'............开始解析动态............'+self.urllieb[j])
                content =requests.get(self.urllieb[j]).content.decode("utf8")
                if re.match(r'http://qc.wa.news.cn/nodeart/list.*', self.urllieb[j]):
                    content = content[1:-2]
            # 将字符串形式的字典转化为真正的字典
                    content = json.loads(content)
                    for item in content['data']['list']:
                        LinkUrl = item['LinkUrl']
                        yield scrapy.Request(LinkUrl, callback=self.parse)
                else:
                    soup = BeautifulSoup(content, "lxml")
                    logtools.write_err(u'开始爬取5464656465')
                    Urls = []
                    urls = soup.find_all('a', href=True)
                    logtools.write_err(u'开始爬取55')
                    for url in urls:
                        u = (url['href'])
                        Urls.append(u)
                    print(Urls)
                    logtools.write_err(u'开始爬取')
                    vaild_urls = filter_invalid_urls(Urls)

                    for url in vaild_urls:
                        yield Request(url, callback=self.parse)
        else:
             urls = first_sel.xpath('//a/@href').extract()
             vaild_urls = filter_invalid_urls(urls)
             for url in vaild_urls:
                 yield Request(url,callback=self.parse)

    def parse_page(self,response,ctype,url_type):
        item = XinhuaItem()
        urls = response.url
        logtools.write_info(u'开始爬取' + urls)

        item['url'] = urls
        item['html_code'] = response.body
        hsel = Selector(response)
        item['encoding'] = 'utf-8'
        item['ctype'] = ctype
        item['subtype'] = url_type
        parsePage(item, hsel, url_type)
        item['originality'] = item['source']
        item['copyright'] = item['source']
        item['type1'] = 'text'
        item['crawltime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        logtools.write_info(urls + u'爬取结束')
        return item
