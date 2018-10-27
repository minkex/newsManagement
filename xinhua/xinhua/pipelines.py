# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from kafka import KafkaProducer
import uuid
import json
import random
import time
import pymysql as ps
from scrapy.shell import inspect_response
from xinhua.logs import logtools
import requests
class ZhongxinPipeline(object):
    def process_item(self,item,spider):
        url = item['url']
        title = item['title']
        time = item['time']
        dd = item['time'].split(" ")
        time=dd[0] + "T" + dd[1] + ":00Z"
        source = item['source']
        editor = item['editor']
        ctype = item['ctype']
        subtype = item['subtype']
        keywords = item['keywords']
        abstract = item['abstract']
        authors1 = item['authors']
        content = item['content'].replace('null', '')
        eventId=str(random.randint(1, 10))
        evenLinetId=str(random.randint(1, 10))
        '''
        r = requests.post(
        'http://223.3.93.101:9000/?properties=%7B%22annotators%22%3A%20%22tokenize%2Cssplit%2Cner%22%2C%20%22date%22%3A%20%222018-09-28T15%3A00%3A22%22%7D&pipelineLanguage=zh',
        data=content.encode('utf-8'),timeout=10)
        if r.status_code==200:
            logtools.write_sys("分词正确：")
        else:
            logtools.write_sys("分词错误：")
        resp = json.loads(r.content.decode('utf-8'))
        data = ''
        characteristics = ''
        for sentence in resp['sentences']:

            tokens = sentence['tokens']
            for j in range(len(tokens)):
                data1 = tokens[j]['word'] + ' '
                if not 'pos' in tokens[j]:
                    pos = ' '
                else:
                    pos = tokens[j]['pos']
                if not 'ner' in tokens[j]:
                    ner = ' '
                else:
                    ner = tokens[j]['ner']
                characteristic = '(' + pos + ',' + ner + ')' + ' '
                data += data1
                characteristics += characteristic
        logtools.write_err(data)
            '''

        id=str(uuid.uuid1())
        data = {"add": {"doc": {
            "id":id,
            "content":content,
            "time":time,
            "title":title,

            }}}
        params = {"boost": 1.0, 'overwrite': 'true', "commitWithin": 1000}
        url = "http://223.3.93.101:8983/solr/news/update?_=1538124510610&commitWithin=1000&overwrite=true&wt=json"
        headers = {"Content-Type": "application/json"}
        r= requests.post(url, json=data, params=params, headers=headers)
        if r.status_code == 200:
            logtools.write_info("插入正确：")
            producer = KafkaProducer(bootstrap_servers='seu:9092',
                                     value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            producer.send('new-docId-input', {
                "doc_id": str(id)
            })
            producer.flush()
        else:
            logtools.write_info("插入错误：")



'''
class ZhongxinPipeline(object):

    def __init__(self):
        try:
            self.conn = ps.connect(host='localhost', user='root', password='root', db='ContentManagement')
        except:
            logtools.write_err(u'数据库连接失败')
            print('数据库连接失败')
        else:
            logtools.write_err(u'数据库连接成功')
            self.cursor = self.conn.cursor()
            #self.cursor.execute("truncate table xinhua")
            #self.conn.commit()


    def close_spider(self, spider):
        self.conn.close()
    def process_item(self, item, spider):
        url = item['url']
        title = item['title']
        time = item['time']
        source = item['source']
        editor = item['editor']
        ctype = item['ctype']
        subtype = item['subtype']
        keywords = item['keywords']
        abstract = item['abstract']
        authors1 = item['authors']
        content = item['content'].replace('null' ,'')
        logtools.write_sys('--------------------------------------------------')
        logtools.write_sys(u'开始存储数据.....' + url)
        if len(content) >= 2:
            try:

                self.cursor.execute(
                    'insert into xinhuanews (url,title,authors,time,source,editor,ctype,subtype,keywords,abstract,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (url, title, authors1, time, source, editor, ctype, subtype, keywords, abstract, content))
                self.conn.commit()
                print(url)
            except:
                logtools.write_err(url + u"数据存储失败")
        logtools.write_sys(url + u'数据存储结束')
        logtools.write_sys('--------------------------------------------------')
        return item
'''
'''
class XinhuaPipeline(object):

    def __init__(self):
        try:
            self.conn = ps.connect(host='localhost', user='root', password='root', db='ContentManagement')
        except:
            logtools.write_err(u'数据库连接失败')
            print('数据库连接失败')
        else:
            logtools.write_err(u'数据库连接成功')
            self.cursor = self.conn.cursor()
            #self.cursor.execute("truncate table xinhua")
            #self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()
    def process_item(self, item, spider):
        if spider.name=='xinhuaTest':
            url = item['url']
            title = item['title']
            time = item['time']
            source = item['source']
            editor = item['editor']
            ctype = item['ctype']
            subtype = item['subtype']
            keywords = item['keywords']
            abstract = item['abstract']
            authors1 = item['authors']
            content = item['content']
            logtools.write_sys('--------------------------------------------------')
            logtools.write_sys(u'开始存储数据.....' + url)
            print('开始存储数据.....' + title)
            if len(content) >= 2:
                try:
                    print(33333)
                    self.cursor.execute(
                        'insert into xinhua (url,title,authors,time,source,editor,ctype,subtype,keywords,abstract,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (url, title, authors1, time, source, editor, ctype, subtype, keywords, abstract, content))
                    print('hahha')
                    print('\n')
                    self.conn.commit()
                except:

                    print('数据存储失败')
                    logtools.write_err(url + u"数据存储失败")
            logtools.write_sys(url + u'数据存储结束')
            logtools.write_sys('--------------------------------------------------')
            print('数据存储结束')
            return item
        elif spider.name=='zhongxin':
            url = item['url']
            title = item['title']
            time = item['time']
            source = item['source']
            editor = item['editor']
            ctype = item['ctype']
            subtype = item['subtype']
            keywords = item['keywords']
            abstract = item['abstract']
            authors1 = item['authors']
            content = item['content']
            logtools.write_sys('--------------------------------------------------')
            logtools.write_sys(u'开始存储数据.....' + url)
            print('开始存储数据.....' + title)
            if len(content) >= 2:
                try:
                    print(33333)
                    self.cursor.execute(
                        'insert into xinhua (url,title,authors,time,source,editor,ctype,subtype,keywords,abstract,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (url, title, authors1, time, source, editor, ctype, subtype, keywords, abstract, content))
                    print('hahha')
                    print('\n')
                    self.conn.commit()
                except:

                    print('数据存储失败')
                    logtools.write_err(url + u"数据存储失败")
            logtools.write_sys(url + u'数据存储结束')
            logtools.write_sys('--------------------------------------------------')
            print('数据存储结束')
            return item
            '''

