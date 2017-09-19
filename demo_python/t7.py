#!/usr/bin/env python
#coding: utf-8
from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 要分析的网页url
#url = 'http://c.itcast.cn/index.html'
#url = 's://user.qzone.qq.com/862983319/infocenter?via=toolbar'
url = 'https://user.qzone.qq.com/862983319/main'
#url = 'http://user.qzone.qq.com/862983319/infocenter?via=toolbar'

def extract(url):
    '''
    提取网页正文
    '''
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == '__main__':
    print extract(url)
