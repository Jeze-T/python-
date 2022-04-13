#import codecs
#import csv
import requests
import xlwt  # 进行excel操作
from lxml import etree
import os
import time

def main():
    baseurl = "https://movie.douban.com/top250?start="  #要爬取的网页链接
    #爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影Top250.xls"    #当前目录新建XLS，存储进去
    #保存数据
    saveData(datalist,savepath)
    download_image(datalist)
    pass

#下载海报
def download_image(datalist):
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "BIDUPSID=3462ADA9DAD1297B8A802A091F3A1F8D; PSTM=1604243305; __yjs_duid=1_bfdc1ab59d6e702f682925e36cc331711619834907464; MAWEBCUID=web_tOeXvJOFvBhPSCMjgshotDYrrvLDyQzIDKDrUBappiXmaMLHMC; BAIDUID=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BDSFRCVID_BFESS=NX0OJeC62rO8dvbHli0nesnLjeh8gWrTH6aohfLyJalmWqO7YODEEG0Phf8g0Ku-hD88ogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nwynR9aJ5nJDoK8Ing5451h-cQhxoe2f7B5C-O0M3-QpP-HJ7dbxvBy4_jhJJDW5bkB2n4Kl0MLnntbb0xyn_VMM3beMnMBMnrteOnan673fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-Xjj30jN3P; BAIDUID_BFESS=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BD_UPN=12314753; baikeVisitId=1b4b0792-99b6-4e00-a829-3a3e32ac4c2c; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1344_0_8_9_10_41_0_2_8_7_4_0_1557297_0_0_0_1644224812_0_1644980831%7C9%23517117_127_1639885104%7C9; H_PS_645EC=61628yiJhNsbuOC4w8F8sM2WXJUfqIFOSNfz1QZvkaRrdLrB2jynmCCk94A; BD_HOME=1; H_PS_PSSID=35105_31253_35766_35865_34584_35490_35872_35245_35796_35317_26350_35746; BA_HECTOR=85800184810084agql1h0pdv80q"
    }
    for i in range(0,250):
        data = datalist[i]
        url = data[1][0]
        #print(url)
        #time.sleep(1)  # 避免大规模访问
        file_name = data[2]
        response = requests.get(url, headers=headers)  # 这个是请求图片
        dir_name = '海报'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        with open(dir_name + '/' + file_name + '.png', "wb") as f:  # 加/是为了体现目录的替换
            f.write(response.content)
# 爬取网页
def getData(baseurl):
    datalist = []  #用来存储爬取的网页信息
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        #逐一解析数据
        for item in html.xpath("//div[@class='item']"):  # 查找符合要求的字符串
            data = []  # 保存一部电影所有信息
            link = item.xpath("(.//a/@href)[1]")
            data.append(link)
            imgSrc = item.xpath(".//img/@src")
            data.append(imgSrc)
            titles = item.xpath(".//span[@class='title']/text()")
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  #消除转义字符
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            rating = item.xpath(".//span[@class='rating_num']/text()")
            data.append(rating)
            judgeNum = item.xpath("translate(.//span[contains(text(),'评价')]/text(),'人评价','')")
            data.append(judgeNum)
            inq = item.xpath(".//span[@class='inq']/text()")
            data.append(inq)
            bd = item.xpath("normalize-space(.//p[@class=''])")
            data.append(bd)
            datalist.append(data)

    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "BIDUPSID=3462ADA9DAD1297B8A802A091F3A1F8D; PSTM=1604243305; __yjs_duid=1_bfdc1ab59d6e702f682925e36cc331711619834907464; MAWEBCUID=web_tOeXvJOFvBhPSCMjgshotDYrrvLDyQzIDKDrUBappiXmaMLHMC; BAIDUID=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BDSFRCVID_BFESS=NX0OJeC62rO8dvbHli0nesnLjeh8gWrTH6aohfLyJalmWqO7YODEEG0Phf8g0Ku-hD88ogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nwynR9aJ5nJDoK8Ing5451h-cQhxoe2f7B5C-O0M3-QpP-HJ7dbxvBy4_jhJJDW5bkB2n4Kl0MLnntbb0xyn_VMM3beMnMBMnrteOnan673fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-Xjj30jN3P; BAIDUID_BFESS=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BD_UPN=12314753; baikeVisitId=1b4b0792-99b6-4e00-a829-3a3e32ac4c2c; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1344_0_8_9_10_41_0_2_8_7_4_0_1557297_0_0_0_1644224812_0_1644980831%7C9%23517117_127_1639885104%7C9; H_PS_645EC=61628yiJhNsbuOC4w8F8sM2WXJUfqIFOSNfz1QZvkaRrdLrB2jynmCCk94A; BD_HOME=1; H_PS_PSSID=35105_31253_35766_35865_34584_35490_35872_35245_35796_35317_26350_35746; BA_HECTOR=85800184810084agql1h0pdv80q"
    }

    response = requests.get(url, headers=headers)
    html_doc = response.content.decode("utf-8")
    html = etree.HTML(html_doc)
    return html

# 保存数据到表格
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) #创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True) #创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,250):
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据
    book.save(savepath) #保存

'''
    file_csv = codecs.open('豆瓣电影Top250', 'w+', 'utf-8')  # 追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, 250):
        data = datalist[i]
        writer.writerow(data)
    print("保存文件成功，处理结束")
'''

if __name__ == '__main__':
    main()
    print("爬取完毕！")