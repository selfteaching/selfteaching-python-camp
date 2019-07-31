from mymodule import stats_word
import logging
from os import path
import json
import jieba

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')   
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems


def main():
    data = load_file()
    poems = merge_poems(json.loads(data)) 
    print(stats_word.stats_text_cn(poems, 100)) 


if __name__ == '__main__':
    main()
