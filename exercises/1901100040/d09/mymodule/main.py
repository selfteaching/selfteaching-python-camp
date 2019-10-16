import stats_word
from os import path
file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json') #获取同一文件夹下文件路径
f = open(file_path)
with open(file_path,'r', encoding='utf-8') as f:
    f.closed
    try:
        print('文件中汉字词频最高的前100个词：\n',stats_word.stats_text_cn(f.read(),100))
    except ValueError:
        print('Error:文本为非字符串')