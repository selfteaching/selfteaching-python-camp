import json#加载json模块完成对.json文件的读取
import stats_word
from os import path#调用os模块中的path函数以获得文件路径
print('请输入要统计的唐诗三百首的词频前多少位：')
filepath = path.join(path.dirname(path.abspath(__file__)),'tang300.json')#join用于合成路径，dirname用于传递目录路径，abspath用于获取main.py所在目录路径，最后加上文件路径就是完整的路径了
with open(filepath,encoding = 'utf-8')as a:#打开文件
    b = json.load(a)#将json文件转换为python文件
a = str(b)#将转换后的字典转换为字符串
print(stats_word.stats_text_cn(a,input()))#调用函数，由用户输入要打印的词频排行位数