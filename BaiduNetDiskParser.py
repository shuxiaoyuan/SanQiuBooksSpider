#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/12/17 15:36
# @Description: 百度网盘链接解析


import logging
from html.parser import HTMLParser


class BaiduNetDiskParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__is_span = False
        self.__is_font = False
        self.__href = None
        self.__code = None

    def handle_starttag(self, tag, attrs):

        if tag == 'span':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'downfile':
                    self.__is_span = True
                    self.__is_font = False
                    return
        elif tag == 'a':
            if self.__is_span:
                self.__is_span = False
                self.__is_font = False
                for attr in attrs:
                    if attr[0] == 'href':
                        self.__href = attr[1]
                        logging.info(self.__href)
                        return
        elif tag == 'font':
            self.__is_span = False
            for attr in attrs:
                if attr[0] == 'style' and attr[1] == 'color: #7B68EE;font-weight: bold;':
                    self.__is_font = True
                    return

        self.__is_span = False
        self.__is_font = False

    def handle_data(self, data):
        if self.__is_font:
            data = data.strip()
            if data:
                self.__code = data
                logging.info(self.__code)

    @property
    def href(self):
        return self.__href

    @property
    def code(self):
        return self.__code

    def error(self, message):
        logging.info(message)
