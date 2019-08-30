from mymodule import stats_word
from os import path
import json
import re
import logging

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
    print('当前文件路径:', __file__, '\n读取文件路径:', file_path)

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems

def main():
    try:
        data = load_file()
        logging.info(data[0])
        poems = merge_poems(json.loads(data))
        logging.info('result ==> %s', stats_word.stats_text_cn(poems, 100))
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()
    
