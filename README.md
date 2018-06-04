# Python 抓取中国行政区划信息

日期：20180605
项目介绍：使用 Python 和 requests、lxml、xlwt 等第三方库抓取中国行政区划信息

抓取的网站：[2016年统计用区划代码和城乡划分代码](view-source:http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html)

## 项目文档介绍

```txt
| - data/：存放项目抓取的 excel 文件
| - resources/：存放 README 的资源文件
| - get_city.py
| - get_county.py
| - get_province.py
| - README.md：使用说明
```

## 项目存在的问题

- 县级市 excel 中有存在数据丢失
