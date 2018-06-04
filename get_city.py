import requests
from lxml import etree
import xlwt
import time

city_info_list=[]
index_url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

def get_province_url(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    province_urls=selector.xpath('//tr[@class="provincetr"]/td/a[1]')
    for province_url in province_urls:
        province_url=index_url+province_url.xpath('@href')[0]
        get_city_url(province_url)

def get_city_url(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    city_urls=selector.xpath('//tr[@class="citytr"]')
    for city_url in city_urls:
        city_code=city_url.xpath('td[1]/a/text()')[0]
        city_name=city_url.xpath('td[2]/a/text()')[0].encode('iso8859').decode('gb2312')
        city_info_list.append([city_code,city_name])
    province_code=url.split('/')[-1].split('.')[0]+'0000000000'
    print('get city: {} success'.format(province_code))

if __name__=='__main__':
    get_province_url(index_url)
    header=['地级市代码','地级市名称']
    book=xlwt.Workbook(encoding='utf8')
    sheet=book.add_sheet('地级市表')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for info_list in city_info_list:
        j=0
        for data in info_list:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('./data/地级市.xls')