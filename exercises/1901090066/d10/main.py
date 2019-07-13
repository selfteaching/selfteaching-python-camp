from mymodule import state_word
from os import path
file_path = path.join(path.dirname(path.realpath(__file__)), 'tang300.json')
fo= open(file_path, 'r', encoding='utf-8')
text=fo.read()
fo.close
try:
    print('统计出现最多的前20词：',state_word.stats_text_cn(text,20))
except ValueError :
    print('输入异常') 

