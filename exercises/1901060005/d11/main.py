from mymodule import stats_word #从mymodule中导入stats_word
from collections import Counter
import re #调取re函数
import os #调取os函数
import jieba
import requests
import yagmail
response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
#print(response)
from pyquery import PyQuery #调用函数
document = PyQuery(response.text)#解析网页内容
#print (document)
content = document('#js_content').text()
#print (content)
seg_list1 = jieba.cut(''.join(content), cut_all=False)#将t1转换字符串再进行jieba
cn1 = []#定义一个空列表
for i in seg_list1:#遍历老列表
    if len(i)>=2:#将字符串长度大于等于2的字符筛选出来
        cn1.append(i)#生成新列表
mydict = Counter(cn1).most_common(100)#统计出现频次前100的字符
print (mydict)
list1=[str(i) for i in mydict]#将列表中的元素转化为字符串
#print (list1)
#print (type(mydict))
strmy =' '.join(list1)#列表转化为字符串
print (strmy)#打印字符串
try:
    stats_word.stats_text(content)
except ValueError:
    print('Input is not str. try again')

yag = yagmail.SMTP('dzhg1013@126.com','dzhg1013')
yag.send('pythoncamp@163.com', '自学营5群 day11 zhiguodavid', strmy)