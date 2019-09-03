#coding = utf-8

from collections import Counter 

 #collections 是python内建的集合模块，Counter 是其中的一个函数,需要用到from...import...  否则counter函数出现Undefined的情况     

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #禁用安全证书，解决InsecureRequestWarning

url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(url)                                        # 最基本的GET请求


from pyquery import PyQuery
document = PyQuery(response.text)
content =document('#js_content').text()                             #从网页中获取文本


count =100
def stats_text_en (content, count):               #定义：函数+括弧；限制输出元素个数
    if not isinstance(content,(str)):             #参数检查
        raise ValueError('bad operand type')   #抛出错误

    replace_text = content.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ').replace('\n','')  #第一步：去掉标点符号
    lower_text = replace_text.lower()          #单词全改为小写/大写
    split_text = lower_text.split()            #文本字符串拆分为用空格隔开的列表

    c = Counter()               #Counter函数统计词频
    for word1 in split_text:                       
        c[word1] += 1            

    c.most_common()             #括号内为输入数字，默认输出全部的单词词频
    return c
print(stats_text_en (content, count))



import jieba                     #导入结巴

def stats_text_cn(content,count):     
    if not isinstance(content,(str)):
        raise ValueError('bad operand type')

    seg_list = jieba.lcut(content, cut_all=False)        #调用jieba method 分词成列表   
    seg_dic = dict([(word ,seg_list.count(word)) for word in seg_list if len(word)>=2])  #遍历seg_list,生成词典，key>=2  来源：issues/1734
    return Counter(seg_dic).most_common(count)
print(stats_text_cn(content,count))  



def stats_text(content,count):
    '''合并统计英文词频和中文词频'''
    if not isinstance(content,str):
        raise ValueError('bad operand type')


print(stats_text_cn (content,count)+stats_text_cn (content,count))