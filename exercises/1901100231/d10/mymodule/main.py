import json#加载json模块完成对.json文件的读取
import stats_word
import jieba
from os import path#调用os模块中的path函数以获得文件路径
filepath = path.join(path.dirname(path.abspath(__file__)),'tang300.json')#join用于合成路径，dirname用于传递目录路径，abspath用于获取main.py所在目录路径，最后加上文件路径就是完整的路径了
with open(filepath,encoding = 'utf-8')as a:#打开文件
    b = a.read()
a=''
for i in json.loads(b):
    a += i.get('contents','')#获取文件中contents的内容，防止标题和作者干扰词频统计
print('唐诗三百首词频前20位：')
print(stats_word.stats_text_cn(a,20))#打印前20位的词频


