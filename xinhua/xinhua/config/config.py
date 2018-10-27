import os
import datetime
from bs4 import BeautifulSoup
from xinhua.logs import logtools
import inspect
this_file=inspect.getfile(inspect.currentframe())
path=os.path.abspath(os.path.dirname(this_file))
try:
    logtools.write_sys("读取并解析配置文件configure.xml开始")

    txt=open(path+os.sep+"config",encoding='utf-8').read()
    soup=BeautifulSoup(txt,"lxml")
    logtools.write_sys("读取并解析配置文件configure.xml结束")
except:
    logtools.write_err("配置文件configure.xml不存在、或者解析出错")
    exit(0)
class mysql:
    host=soup.xml.mysql.host
    port=soup.xml.mysql.port
    user=soup.xml.mysql.user
    password=soup.xml.mysql.password
    database=soup.xml.mysql.database
    filetable=soup.xml.mysql.host
    ucltable=soup.xml.mysql.host
class website_info:
    crawler_depth = int(soup.xml.crawler_depth.string)
    crawler_delay = int(soup.xml.crawler_delay.string)
    start_urls=[]
    allowed_domains=[]
    LinkURL=[]
    zhongxinURLS=[]
    date_list = []
    for start_url in soup.xml.configuration.urls.start_urls.find_all("start_url"):
        start_urls.append(start_url.string)

    for dynamic in soup.find_all(id="dynamic_link"):
        link=dynamic.crawl.link.next_element
        nid=dynamic.crawl.nid.string
        cnt=dynamic.crawl.cnt.string
        tp=dynamic.crawl.tp.string
        orderby=dynamic.crawl.tp.string
        pgnum=dynamic.crawl.pgnum.string
        for i in range(1,int(pgnum)+1):
            u=str(link)+'nid='+str(nid)+'&pgnum='+str(i)+'&cnt='+str(cnt)+'&tp='+str(tp)+'&orderby'+str(orderby)+'?'
            LinkURL.append(u)
    for static in soup.find_all(id="static_link"):
        link=static.crawl.link.next_element
        LinkURL.append(link)
    for zhongxinURL in soup.find_all(id="zhongxin_link"):
        link=zhongxinURL.link.next_element
        pgnum=zhongxinURL.pgnum.string
        begin_date=zhongxinURL.begin_date.string
        end_date=zhongxinURL.end_date.string
        begin_date = datetime.datetime.strptime(begin_date, "%Y/%m%d")
        end_date = datetime.datetime.strptime(end_date, "%Y/%m%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y/%m%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        for i in range(1,int(pgnum)+1):
            u=str(link)+'news'+str(i)+'.html'
            '''zhongxinURLS.append(u)'''
        for date in date_list:
            zhongxinURLS.append(str(link)+date+'/news.shtml')


    def get_URLs(self):

        return self.LinkURL
    def get_zhongxinURLS(self):
        return self.zhongxinURLS

class detail_info:
    url_depth = \
        int(soup.xml.configuration.parse_rules.detail_rules.url_depth.string)
    detail_rule = soup.xml.configuration.parse_rules.detail_rules
    date_rules = {}
    for date_rule in detail_rule.date_rule.find_all("rule"):
        date_rules[date_rule.rule_id.string] = date_rule.regex.string

    allowed_channels = {}
    for channel in detail_rule.allowed_channels.find_all('channel'):
        channel_rules = {}
        channel_rules['ctype'] = channel.attrs['ctype']
        public_rule = detail_rule.public_rules
        # 解析关键词
        keywords_rules = {}
        krule_list = public_rule.keywords_rules.find_all('rule')
        krule_list.extend(channel.keywords_rules.find_all('rule'))
        for k_rule in krule_list:
            keywords_rules[k_rule.rule_id.string] = {}
            keywords_rules[k_rule.rule_id.string]['rule'] = k_rule.xpath.string
            keywords_rules[k_rule.rule_id.string]['sep'] = k_rule.sep.string
        channel_rules['keywords_rules'] = keywords_rules
            # 解析摘要
        abstract_rules = {}
        arule_list = public_rule.abstract_rules.find_all('rule')
        arule_list.extend(channel.abstract_rules.find_all('rule'))
        for a_rule in arule_list:
            abstract_rules[a_rule.rule_id.string] = {}
            abstract_rules[a_rule.rule_id.string]['rule'] = a_rule.xpath.string
        channel_rules['abstract_rules'] = abstract_rules
            # 解析编辑
        editor_rules = {}
        edrule_list = public_rule.editor_rules.find_all('rule')
        edrule_list.extend(channel.editor_rules.find_all('rule'))
        for ed_rule in edrule_list:
            editor_rules[ed_rule.rule_id.string] = {}
            editor_rules[ed_rule.rule_id.string]['rule'] = ed_rule.xpath.string
            editor_rules[ed_rule.rule_id.string]['regex'] = ed_rule.regex.string
            editor_rules[ed_rule.rule_id.string]['pprefix'] = \
                ed_rule.pprefix.string
        channel_rules['editor_rules'] = editor_rules
        # 解析标题
        title_rules = {}
        tirule_list = public_rule.title_rules.find_all('rule')
        tirule_list.extend(channel.title_rules.find_all('rule'))
        for ti_rule in tirule_list:
            title_rules[ti_rule.rule_id.string] = {}
            title_rules[ti_rule.rule_id.string]['rule'] = ti_rule.xpath.string
        channel_rules['title_rules'] = title_rules
            # 解析时间
        time_rules = {}
        tmrule_list = public_rule.time_rules.find_all('rule')
        tmrule_list.extend(channel.time_rules.find_all('rule'))
        for tm_rule in tmrule_list:
            time_rules[tm_rule.rule_id.string] = {}
            time_rules[tm_rule.rule_id.string]['rule'] = tm_rule.xpath.string
            time_rules[tm_rule.rule_id.string]['regex'] = tm_rule.regex.string
            time_rules[tm_rule.rule_id.string]['temp'] = tm_rule.temp.string
        channel_rules['time_rules'] = time_rules
        # 解析来源
        source_rules = {}
        rule_list = public_rule.source_rules.find_all('rule')
        rule_list.extend(channel.source_rules.find_all('rule'))
        for irule in rule_list:
            source_rules[irule.rule_id.string] = {}
            source_rules[irule.rule_id.string]['rule'] = irule.xpath.string
            source_rules[irule.rule_id.string]['regex'] = irule.regex.string
            source_rules[irule.rule_id.string]['pprefix'] = \
                irule.pprefix.string
        channel_rules['source_rules'] = source_rules
            # 解析内容
        content_rules = {}
        rule_list = public_rule.content_rules.find_all('rule')
        rule_list.extend(channel.content_rules.find_all('rule'))
        for irule in rule_list:
            content_rules[irule.rule_id.string] = {}
            content_rules[irule.rule_id.string]['rule'] = irule.xpath.string
            channel_rules['content_rules'] = content_rules
            # 解析图片
        img_rules = {}
        rule_list = public_rule.img_rules.find_all('rule')
        rule_list.extend(channel.img_rules.find_all('rule'))
        for irule in rule_list:
            img_rules[irule.rule_id.string] = {}
            img_rules[irule.rule_id.string]['rule'] = irule.xpath.string
        channel_rules['img_rules'] = img_rules

        allowed_channels[channel.attrs['name']] = channel_rules

if __name__=='__main__':
    web=website_info()
    print(web.get_zhongxinURLS())


