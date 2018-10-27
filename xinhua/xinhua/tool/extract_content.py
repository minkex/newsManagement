# -*- coding: utf-8 -*-
import re
from xinhua.config.config import detail_info

def tidy_content(items):
	content = ''
	for item in items:
		citem = item.replace('\n','').rstrip()
		if filterParag(citem):
			content += citem+'\n'
	return content

def parsecontent(hsel,url_type):
	content_rules = detail_info.allowed_channels[url_type]['content_rules'].values()
	for rule in content_rules:
		itemcontent = hsel.xpath(rule['rule'])
		infocontent = itemcontent.xpath('string(.)').extract()
		if len(infocontent)>0:
			return tidy_content(infocontent)
	return ''


def filterParag(parag):
	rule = re.compile(u'\xe8\xae\xb0\xe8\x80\x85')
	if parag == '':
		return False
	if parag == u'\u3000\u3000':
		return False
	if re.match(rule,parag.strip())!= None:
		return False
	return True
