#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/16 13:56
# @Description: 三秋书屋爬虫

import logging
import time
from urllib import request
from IDParser import IDParser
from BaiduNetDiskParser import BaiduNetDiskParser
logging.basicConfig(level=logging.INFO)


def crawl(url):
    with request.urlopen(url) as r:
        return r.read().decode('utf-8')


# 爬取 id
url_id = 'https://www.d4j.cn/xuexi-ganhuo/biancheng-kaifa'
parser_id = IDParser()
parser_id.feed(crawl(url_id))
# for i in range(2, parser_id.total_pages + 1):
#     time.sleep(1)
#     parser_id.feed(crawl(url_id + ('/page/%s' % i)))
book_dict_ordered = parser_id.book_dict_ordered
parser_id.close()

# 根据 id 爬取网盘链接和提取码
url_baidu_net_disk = 'https://www.d4j.cn/download.php?id=%s'
parser_baidu_net_disk = BaiduNetDiskParser()
book_list = []
for book_id, book_name in book_dict_ordered.items():
    time.sleep(1)
    parser_baidu_net_disk.feed(crawl(url_baidu_net_disk % book_id))
    book_list.append((book_dict_ordered[book_id], parser_baidu_net_disk.href, parser_baidu_net_disk.code))
parser_baidu_net_disk.close()

for book in book_list:
    print(book)
