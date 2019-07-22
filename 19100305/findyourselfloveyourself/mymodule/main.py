import stats_word
import json
from os import path
import re

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)),'./tang300.json')
    print('当前文件路径：',__file__,'\n读取文件路径：',file_path)
    with open(file_path,'r',encoding='utf-8') as text:
    #try:
        #stats_word.stats_text(text)
    #except ValueError:
        #print('输入参数不为字符串类型')
    #print(text)
    
        return text.read()
text = load_file()
print(stats_word.stats_text_cn(text,20))