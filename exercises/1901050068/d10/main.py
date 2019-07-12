from os import path

print(__file__, __name__)

fp = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')    # 读取文件
with open(fp, 'r') as f:  
    text = f.read()

import stats_word 

count = 100

try:  
    print(f'输出词频最高的前100个汉字：{stats_word.stats_text_cn(text,count)}')    

except Exception as e:  # 检查中英文词频异常
    print('ValueError =>', e)


    
