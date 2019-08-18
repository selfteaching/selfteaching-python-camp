import json#加载json模块完成对.json文件的读取
import stats_word
print('请输入要统计的唐诗三百首的词频前多少位：')
a = open('D:/Git hub/selfteaching-python-camp/exercises/1901100231/d09/mymodule/tang300.json',encoding = 'utf-8')#打开文件
b = json.load(a)#将json文件转换为python文件
a = str(b)#将转换后的字典转换为字符串
print(stats_word.stats_text_cn(a,input()))#调用函数，由用户输入要打印的词频排行位数