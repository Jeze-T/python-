#发送一次普通的get请求并接收
import requests

def main():
    url = "http://www.baidu.com"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
               "Connection":"keep-alive",
               "Cookie":"BIDUPSID=3462ADA9DAD1297B8A802A091F3A1F8D; PSTM=1604243305; __yjs_duid=1_bfdc1ab59d6e702f682925e36cc331711619834907464; MAWEBCUID=web_tOeXvJOFvBhPSCMjgshotDYrrvLDyQzIDKDrUBappiXmaMLHMC; BAIDUID=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BDSFRCVID_BFESS=NX0OJeC62rO8dvbHli0nesnLjeh8gWrTH6aohfLyJalmWqO7YODEEG0Phf8g0Ku-hD88ogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nwynR9aJ5nJDoK8Ing5451h-cQhxoe2f7B5C-O0M3-QpP-HJ7dbxvBy4_jhJJDW5bkB2n4Kl0MLnntbb0xyn_VMM3beMnMBMnrteOnan673fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-Xjj30jN3P; BAIDUID_BFESS=0C57B51E04C945AEB6A3FC64443905E9:FG=1; BD_UPN=12314753; baikeVisitId=1b4b0792-99b6-4e00-a829-3a3e32ac4c2c; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=1344_0_8_9_10_41_0_2_8_7_4_0_1557297_0_0_0_1644224812_0_1644980831%7C9%23517117_127_1639885104%7C9; H_PS_645EC=61628yiJhNsbuOC4w8F8sM2WXJUfqIFOSNfz1QZvkaRrdLrB2jynmCCk94A; BD_HOME=1; H_PS_PSSID=35105_31253_35766_35865_34584_35490_35872_35245_35796_35317_26350_35746; BA_HECTOR=85800184810084agql1h0pdv80q",
               "Host":"www.baidu.com"}
    #如果POST 需要带data，GET带参数 Params  循环for i in range(2);  ?id={}".format("3")    和用户互动    代理访问  反反爬虫   cookie session token请求     https   超时   json xml    精确提取某句话……
    # 请求对应的url
    responses = requests.get(url, headers=headers)

    #新建文件并写入网页源代码  （直接打印则print(responses.content.decode("utf-8"))，
    #请求头.request.headers，响应头.headers，响应地址.url，请求地址 .request.url
    with open("pa.txt", "wb") as p:
       p.write(responses.content)
  #  print(responses.content.decode("utf-8"))
    pass

if __name__=='__main__':
    main()

    #直接控制浏览器的方法