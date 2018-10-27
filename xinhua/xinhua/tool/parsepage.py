# -*- coding: utf-8 -*-
from xinhua.tool.extract_content import parsecontent
import time
import re
from xinhua.config.config import detail_info
from xinhua.tool.extract_authors import parse_author
from xinhua.logs import logtools
def parsePage(item,hsel,url_type,url):
    all_rules = detail_info.allowed_channels[url_type]
    #提取标题
    title_rules = all_rules['title_rules'].values()

    for title_rule in title_rules:
        t1 = hsel.xpath(title_rule['rule']).extract()
        if len(t1) > 0:
            item['title'] =t1[0]
            break
        item['title'] = ''
    #提取关键字
    kw_rules = all_rules['keywords_rules'].values()
    for kw_rule in kw_rules:
        kw = hsel.xpath(kw_rule['rule']).extract()
        if len(kw)>0:
            item['keywords'] = kw[0]
            break
        item['keywords'] = ''



    #提取摘要
    abst_rules = all_rules['abstract_rules'].values()
    for abst_rule in abst_rules:
        abst = hsel.xpath(abst_rule['rule']).extract()
        if len(abst)>0:
            item['abstract'] = abst[0]
            break
        item['abstract'] = item['title']
    #提取编辑与作者
    editor_rules = all_rules['editor_rules'].values()
    for rule1 in editor_rules:
         idata = hsel.xpath(rule1['rule']).re(r'编辑\D*')
         if len(idata)>0:
             #idata=re.compile(rule1['regex']).findall(idata[0])
             if len(idata) > 1:
                 item['editor'] = idata[1].encode("utf-8").decode()\
                                .replace(rule1['pprefix'],'').replace('编辑：','').replace('】','').replace('\n','').strip()
             else:
                 item['editor'] = idata[0].encode("utf-8").decode()\
                                .replace(rule1['pprefix'],'').replace('编辑：','').replace('】','').replace('\n','').strip()
                 item['authors'] = item['editor']
                 break
         item['editor'] = ''


    #提取时间
    time_rules = all_rules['time_rules'].values()

    for rule2 in time_rules:
         idata2 = hsel.xpath(rule2['rule']).re(r'(\d{4}年\d{2}月\d{2}日 \d{2}:\d{2})|(\d{4}-\d{2}-\d{2} \d{2}:\d{2})')
         if  len(idata2)>0:
             if '' in idata2:
                 idata2.remove('')
             item['time'] = idata2[0].encode("utf-8").decode().replace('\n','').replace("年","-").replace("月","-").replace("日","").strip()
             break
         item['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

    #解析来源
    source_rules = all_rules['source_rules'].values()
    for rule3 in source_rules:
         idata3 = hsel.xpath(rule3['rule']).extract()
         if  len(idata3)>0:
             idata3=re.compile(rule3['regex']).findall(idata3[0])
             if len(idata3)>0:
                 item['source'] = idata3[0].replace("来源：","").replace(" ","")
                 break
         item['source'] = ''


    #提取图片url
    img_rules = all_rules['img_rules'].values()
    for rule3 in img_rules:
        idata3 = hsel.xpath(rule3['rule']).extract()
        if len(idata3) > 0:
            item['img'] = idata3[0].encode("utf-8").decode().strip()
            break
        item['img']=''
    content=parsecontent(hsel,url_type)
    item['content'] = content
    authors = parse_author(content)
    item['authors'] = item['editor']

if __name__=='__main__':
    all_rules = detail_info.allowed_channels['tp']
    editor_rules = all_rules['editor_rules'].values()
    print(editor_rules)
















