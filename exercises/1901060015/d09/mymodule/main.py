import json
import logging
import re
from os import path

import stats_word

logging.basicConfig(
    format='file:%(filename)s | line:%(lineno)d | message:%(message)s',level=logging.DEBUG)

def load_file():
    flie_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    
    with open(flie_path,'r',encoding='utf-8') as f:
        return f.read()

def merge_poems(data):
    poems =''
    for item in data:
        poems +=item.get('contents','')
    return poems

def main():
    try:
    
        data=load_file()
        logging.info(data[0])
        poems=merge_poems(json.loads(data)).replace("，","").replace("。","").replace("\n","").replace("？","").replace("！","")
        logging.info('result ==> %s',stats_word.stats_text_cn(poems))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()
