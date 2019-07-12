from mymodule import stats_word
from os import path
import json

if __name__ == '__main__':
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')

    with open(file_path, 'r') as f:
        data = f.read()

    poems = ''
    for item in json.loads(data):
        poems += item.get('contents', '')
    
    print('统计中文词频:')
    print(stats_word.stats_text_cn(poems, 20))