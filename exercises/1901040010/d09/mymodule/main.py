

from stats_word import stats_text_cn
import json

f = open('tang300.json','r') 
text = f.read()
f.close()

try:
    print('在《唐诗三百首》中，使用频率最高的前100个字：')
    print(stats_text_cn(text,100))
except ValueError:
    print('检阅内容应为字符')

