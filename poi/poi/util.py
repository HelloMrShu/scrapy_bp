# -*- coding: utf-8 -*-
import re
from urllib import parse


def datamap(data):
    dic = {}
    index = 0
    for item in data:
        item = list(item)
        dic.setdefault(index, item[1])
        index = index + 1
    return dic


def categorymap(data):
    dic = {}
    for item in data:
        item = list(item)
        dic.setdefault(item[1], item[0])
    return dic


def resolve(url):
    url = parse.unquote(url)
    pattern = r'[\u4e00-\u9fa5]+'
    match = re.compile(pattern)
    return match.findall(url)




