#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/16 15:11
# @Description: 先解析所有书的 id

import logging
from html.parser import HTMLParser
from collections import OrderedDict


class IDParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__total_pages = -1
        self.__is_h2 = False
        self.__is_a = False
        self.__book_dict_ordered = OrderedDict()
        self.__book_id = None
        self.__book_name = None
        self.__book_name_ends = '下载'

    def handle_starttag(self, tag, attrs):

        # 初始化总页数
        if self.__total_pages == -1:
            self.__set_total_pages(tag, attrs)

        # 是否有 book 链接标签
        if tag == 'h2':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'kratos-entry-title-new':
                    self.__is_h2 = True
                    self.__is_a = False
                    return
        elif tag == 'a' and self.__is_h2:
            self.__is_a = True
            self.__is_h2 = False
            for attr in attrs:
                if attr[0] == 'href':
                    self.__book_id = (attr[1].split('/')[-1]).split('.')[0]
                    return

        self.__is_h2 = False
        self.__is_a = False

    def __set_total_pages(self, tag, attrs):
        href = ''
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    href = attr[1]
                if attr[0] == 'class' and attr[1] == 'extend':
                    try:
                        self.__total_pages = int(href.split('/')[-1])
                    except BaseException:
                        self.__total_pages = 1
                    return

    def handle_data(self, data):
        # 提取 book_id: book_name 键值对
        if self.__is_a:
            data = data.strip()
            if data.endswith(self.__book_name_ends):
                self.__book_name = data
                self.__book_dict_ordered[self.__book_id] = self.__book_name
                logging.info('%s: %s' % (self.__book_id, self.__book_name))

    @property
    def total_pages(self):
        return self.__total_pages

    @property
    def book_dict_ordered(self):
        return self.__book_dict_ordered

    def error(self, message):
        logging.error(message)
