import requests
from lxml import etree
import xlwt
import time

province_info_list=[]
index_url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

def get_province_url(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    province_urls=selector.xpath('//tr[@class="provincetr"]/td/a')
    for province_url in province_urls:
        province_name=province_url.xpath('text()')[0].encode('iso8859').decode('gb2312')
        province_code=province_url.xpath('@href')[0].split('.')[0]+'0000'
        province_info_list.append([province_code,province_name])
    print('get province success')
    time.sleep(2)

if __name__=='__main__':
    get_province_url(index_url)
    header=['省份代码','省份名称']
    book=xlwt.Workbook(encoding='utf8')
    sheet=book.add_sheet('省份表')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for info_list in province_info_list:
        j=0
        for data in info_list:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('./data/省份.xls')