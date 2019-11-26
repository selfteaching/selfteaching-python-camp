from mymodule import stats_word
from os import path
import json
import re
import logging

logging.basicConfig(  #对logging打印出来的信息做format设置  不是很懂
    format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)
  

def load_file():
    '''
    1 常用获取文件方式，要保证唐诗文件和当前文件在同一文件夹下
    '''
    file_path=path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    print('当前文件路径：',__file__,'\n读取文件路径：',file_path)

    '''
    2 这种方式 表示唐诗文件在当前文件的上一级目录
    file_path=path.join(path.dirname(path.abspath(__file__)),'../tang300.json')
    print(__file__,file_path)

    3 这种方式 表示唐诗文件在当前文件的上一级目录的data文件夹下
    file_path=path.join(path.dirname(path.abspath(__file__)),'../data/tang300.json')
    print(__file__,file_path)
    '''
    
    with open(file_path,'r',encoding='utf-8') as f:  #open是内置方式，utf-8是编码
        return f.read()


def merge_poems(data):
    poems=''
    for item in data:
        poems += item.get('contents','')
    return poems


def main():  # try-except  捕获可能的异常 和  logging+exception 捕获异常
    try:     
        data = load_file()
        #logging.info(data[0])  #显示 打印出字符串的第一个符号， 不懂哦 
        poems=merge_poems(json.loads(data))
        logging.info('result ==> %s',stats_word.stats_text_cn(poems,20))  #不懂哦 ，选取出前20个出现频率最高的字

    except Exception as e:
        logging.exception(e)



if __name__ == "__main__":
    main()
