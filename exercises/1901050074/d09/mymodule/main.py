import os
import stats_word

#print(__file__, __name__)
#print(os.getcwd())
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')    # 读取文件
with open(filepath, 'r',encoding='UTF-8') as f:  
    text = f.read()

count=100
try:
    print(f'输出词频最高的前100个汉字词频：{stats_word.stats_text_cn(text,count)}')
except ValueError:
    print('输入为非字符串,请重新输入。')