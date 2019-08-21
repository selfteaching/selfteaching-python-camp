from os import path
from stats_word import stats_text_cn

print(__file__, __name__)

fp = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')    # 读取文件
with open(fp, 'r', encoding='UTF-8') as f:  
    text = f.read()

count = 20  # 统计前20的词频

try:  
    print(f'输出词频前20的词和词频数：{stats_text_cn(text,count)}')

except Exception as e:  # 检查中文词频异常
    print('ValueError =>', e)

    
