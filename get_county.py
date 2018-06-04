import requests
from lxml import etree
import xlwt

county_info_list=[]
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
    city_urls=selector.xpath('//tr[@class="citytr"]/td/a[1]')
    for city_url in city_urls:
        city_url=index_url+city_url.xpath('@href')[0]
        get_county_url(city_url)

def get_county_url(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    county_urls=selector.xpath('//tr[@class="countytr"]')
    for county_url in county_urls:
        try:
            county_code=county_url.xpath('td[1]/descendant::text()')[0]
            county_name=county_url.xpath('td[2]/descendant::text()')[0].encode('iso8859').decode('gb2312')
            county_info_list.append([county_code,county_name])
        except IndexError:
            print('index error')
            pass
        except UnicodeDecodeError:
            print('decode error')
            pass

if __name__=='__main__':
    get_province_url(index_url)
    header=['县级市代码','县级市名称']
    book=xlwt.Workbook(encoding='utf8')
    sheet=book.add_sheet('县级市表')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for info_list in county_info_list:
        j=0
        for data in info_list:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('./data/县级市.xls')