# -*- coding: utf-8 -*-
import re
import urllib.parse
from xinhua.config.config import detail_info


def filter_invalid_urls(urls):
    valid_urls = []
    rule1 = 'www.chinanews.com'
    for url in urls:
        if len(str(url).strip()) < 10:
            continue
        if str(url).lstrip()[0] == '#':
            continue
        if str(url).lstrip()[:4] == "java":
            continue
        if str(url).lstrip()[:3] == "jpg":
            continue
        if str(url).lstrip()[:3] == "png":
            continue
        if str(url).lstrip()[:4] == "jpeg":
            continue
        if re.search(rule1, url) == None:
            continue
        ctype, utype = getType(url)
        if not ctype:
            continue
        valid_urls.append(url)
    return valid_urls


def isMpage(res_url):
    url_list = res_url.split('/')
    length = len(url_list)
    url_depth = detail_info.url_depth  # 后期使用config
    if length > url_depth:
        hasdate = hasDate(res_url)
        if hasdate:
            ctype, url_type = getType(res_url)
            if ctype:
                return ctype, url_type
            return None, None
        return None, None
    return None, None


def hasDate(url):
    regx = r'/\d{4}/\d{2}-\d{2}/'  # 后期使用config
    if re.search(regx, url) != None:
        return True
    return False


def getType(res_url):
    type_info = detail_info.allowed_channels
    Typelist = type_info.keys()
    # 后期使用config
    for ctype in Typelist:
        if re.search('/'+ctype+'/', res_url):
            return type_info[ctype]['ctype'], ctype
    return None, None


if __name__ == '__main__':
    print(isMpage('http://www.chinanews.com/sh/2016/08-26/7985736.shtml'))








