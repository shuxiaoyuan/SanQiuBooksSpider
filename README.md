# SanQiuBooksSpider

## 用途
使用 Python 内置的 urllib 和 HTMLParser 库爬取[三秋书屋](https://www.d4j.cn)电子书的百度网盘链接和提取码。
## 说明
Python 这两个内置的库都不是很好用，特别是 HTMLParser 解析器，需要自己写很多底层实现，不如 xpath 和 BeautifulSoup 等第三方库使用起来方便，
写这个爬虫仅仅是为了练习这两个库的使用。另外这个网站负载能力比较弱，不要频繁请求。