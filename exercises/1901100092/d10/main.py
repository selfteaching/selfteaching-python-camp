from os import path
import json
from mymodule import stats_word

def load_file():

    file_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    with open(file_path,encoding='utf-8') as f:
        contents = f.read()
    return contents


#text=1                  #验证参数检查功能是否生效
try:
    print(stats_word.stats_text_cn(load_file()))
except ValueError:
    print('stats_text参数应为字符串类型')
