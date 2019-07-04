from mymodule import stats_word
from os import path
import json
import re
import logging

logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)


def load_file():
    '''
    1.
    下面是常用的获取文件路径的方式，要确保tang300.json跟当前文件在同一文件夹下，这两种方式等价
    file_path=path.join(path.dirname(path.abspath(__file__)),'./tang300.json')
    '''
    file_path=path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    print('当前文件路径：',__file__,'\n读取文件路径：',file_path)

    '''
    2.
    这种方式表示tang300.json在当前文件的上一级目录
    file_path=path.join(path.dirname(path.abspath(__file__)),'../tang300.json')
    print(__file__,file_path)

    3.
    这种方式表示tang300.json在当前文件的上一级目录的data文件夹下
    file_path=path.join(path.dirname(path.abspath(__file__)),'../data/tang300.json')
    print(__file__,file_path)
    '''
    with open(file_path,'r',encoding='utf-8')as f:
        return f.read()
    

def merge_poems(data):
    poems=''
    for item in data:
        poems +=item.get('contents','')
    return poems

def main():
    try:
        data=load_file()
        logging.info(data[0])
        poems=merge_poems(json.loads(data))
        logging.info('result==>%s',stats_word.stats_text_cn(poems,100))
    except Exception as e:
        logging.exception(e)


if __name__=="__main__":
    main()







   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
