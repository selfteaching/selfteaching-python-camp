# -*- coding:utf-8 -*-
#  author: yukun
import requests
from bs4 import BeautifulSoup
import random
import time
 
user_agent_list = [
    
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',

'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',


'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',


'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3']

user_agent = random.choice(user_agent_list)
headers  = {
    
    'Cookie':'user_trace_token=20170603115043-d0c257a054ee44f99177a3540d44dda1; LGUID=20170603115044-d1e2b4d1-480f-11e7-96cf-525400f775ce; JSESSIONID=ABAAABAAAGHAABHAA8050BE2E1D33E6C2A80E370FE9167B; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; login=false; unick=""; _putrc=""; _ga=GA1.2.922290439.1496461627; X_HTTP_TOKEN=3876430f68ebc0ae0b8fac6c9f163d45; _ga=GA1.3.922290439.1496461627; LGSID=20170720174323-df1d6e50-6d2f-11e7-ac93-5254005c3644; LGRID=20170720174450-12fc5214-6d30-11e7-b32f-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500541369; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500543655',
    'User-Agent':user_agent,
    'Connection':'keep-alive'
}
proxy_list = [
    'http://140.224.76.21:808',
    'http://60.178.14.90:8081',
    'http://121.232.146.13:9000',
    "http://12.34.56.79:9527",
    ]
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}


base_url = 'https://www.lagou.com/zhaopin/Java/'
for i in range(1,10):
    url = base_url + str(i) + "/"
    # 获取页面源码函数

    resp = requests.get(url, headers=headers, proxies=proxies)
    time.sleep(random.randint(2,10))
    soup = BeautifulSoup(resp.text, 'lxml')
    
    # 职位信息 
    positions = soup.select('ul > li > div.list_item_top > div.position > div.p_top > a > h3')
    print(positions)
        # 工作地址 
'''adds = soup.select('ul > li > div.list_item_top > div.position > div.p_top > a > span > em') 
# 发布时间 
publishs = soup.select('ul > li > div.list_item_top > div.position > div.p_top > span') 
# 薪资信息
moneys = soup.select('ul > li > div.list_item_top > div.position > div.p_bot > div > span') 
# 工作需求 
needs = soup.select('ul > li > div.list_item_top > div.position > div.p_bot > div') 
# 发布公司 
companys = soup.select('ul > li > div.list_item_top > div.company > div.company_name > a') 

tags = soup.select('ul > li > div.list_item_bot > div.li_b_l') 
# 公司福利 
fulis = soup.select('ul > li > div.list_item_bot > div.li_b_r')


for position,add,publish,money,need,company,tag,fuli in zip(positions,adds,publishs,moneys,needs,companys,tags,fulis):
    data = {
    'position' : position.get_text(),
    'add' : add.get_text(),
    'publish' : publish.get_text(),
    'money' : money.get_text(),
    'need' : need.get_text().split('\n')[2],
    'company' : company.get_text(),
    'tag' : tag.get_text().replace('\n','-'),
    'fuli' : fuli.get_text()
    }
    print(data)'''