import stats_word
import json
with open('tang300.json',encoding='utf-8') as f:  #导入tang300.json文件
    text_dic=f.read() #读取内容
text=str(text_dic) #转换成字符串，统计词频的函数需要一个字符串
count=20  #限制输出元素的变量
try: 
    text_list= stats_word.stats_text_cn(text,count) #调用统计汉字的函数
    print(text_list)
except ValueError as identifier: 
    print('请输入字符串',identifier) 

