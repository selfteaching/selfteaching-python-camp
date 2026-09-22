from  mymodule import stats_word
from os import path
import json
import logging

logging.basicConfig(
  format='文件名:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

def load_file():
    file_path=path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    print('当前读取文件路径:',file_path)

    with open (file_path,'r',encoding='utf-8') as f:
         return f.read()

def main():
    try:
        data=load_file()
       # print(data)
        logging.info(data[0])
        data1=json.loads(data)
        poems=''
        for item in data1:
            poems += item.get('contents','')
        logging.info(stats_word.stats_text_cn(poems,100))
    except Exception as e:
        logging.exception(e)
if  __name__ == "__main__":
   main()
