from os import path
import json
import re
import collections
import io
import sys
from collections import Counter               
import jieba
import requests
from pyquery import PyQuery
import getpass
import yagmail

# 获取张小龙演讲链接中的内容

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') 

document = PyQuery(response.text) 
paper_content = document('#js_content').text()


# 中文字频分析

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def stats_text_cn(stri):  
    '''【注】:stats_text_cn()函数为每个汉字统计的次数如下： '''  
    if type(stri) != str:
     raise ValueError("This is not string!")
    dictionary={}                                      
    entext2=""              
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    
         entext2+=i
    #cnt=Counter()
    count=100
    #for i in entext2:  
        #cnt[i]+=1  

    seg_list=jieba.cut(entext2,cut_all=False,HMM=False)
    poem_string = "/".join(seg_list)
    poem_string = poem_string.split("/")
    for i in poem_string:
         dictionary[i] = poem_string.count(i)
    dictionary = collections.Counter(dictionary).most_common(count)
    print(stats_text_cn. __doc__) 
    print(dictionary)
    return dictionary


def main():
    #location = sys.argv[0] #获取main.py的路径
    #location = location.rstrip('main.py') + 'tang300.json' #获取tang300.json的路径

    #with open(location,'r',encoding='UTF-8') as tang_text: #读取文件
        #text = json.load(tang_text) #json转码
    result = {}

    result=stats_text_cn(paper_content)

    result= str(result)

    sender = input('请输入发件人邮箱：')
    password = getpass.getpass('请输入发件人邮箱密码：')
    recipients = 'pythoncamp@163.com'

    yagmail.SMTP(sender,password,'smtp.163.com').send(recipients,'19100401 SunElliot',result)

if __name__ == '__main__':
        main()
