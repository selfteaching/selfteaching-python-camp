
#import stats_word                              #导入stats_word模块。。。/ 也可以用"from stats_word import stats_text"，通过直接导入stats_word模块中的函数stats_text，然后运行函数stats_text(text)   
#import json
#def errorport(test1):
 #   try : 
  #   stats_word.stats_text(test1)
   # except ValueError as error :
    # print(error) 
               
#test_data=[]
#with open('tang300.json','r',encoding='UTF-8') as f:       # 问题：FileNotFoundError: [Errno 2] No such file or directory: 'tang300.json'
# test_date=json.load(f)
#
#for line in f:                                             #设置文件对象并读取每一行文件
 #   test_data.append(line)                                      #将每一行文件加入到list中
#json_str = json.dumps(test_data,indent=5,ensure_ascii=False)
#print(type(json_str))
#errorport(json_str)
#f.close()

#...............................................................

# 下面是第九天作业示例
# 也顺便演示了大家可能会遇到的问题的解决方法

from os import path
import collections
import json
import re


def load_file():
    '''
    1.
    下面是常用的获取文件路径的方式，要确保 tang300.json 跟当前文件在同一文件夹下，这两种方式等价
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
    '''
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
    print('当前文件路径：', __file__, '\n读取文件路径：', file_path)

    '''
    2.
    这种方式表示 tang300.json 在当前文件的上一级目录
    file_path = path.join(path.dirname(path.abspath(__file__)), '../tang300.json')
    print(__file__, file_path)
    3.
    这种方式表示 tang300.json 在当前文件的上一级目录的 data 文件夹下
    file_path = path.join(path.dirname(path.abspath(__file__)), '../data/tang300.json')
    print(__file__, file_path)
    '''

    '''
    读取文件时如果抛出 decode error 之类的错误可以用下面的两种方式替换
    1. with open(file_path, 'rb') as f:
    2. with open(file_path, 'r', encoding='utf-8') as f:
    替换 with open(file_path) as f:
    '''
    with open(file_path) as f:
        return json.load(f)


def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems


def stats_text_cn(text, count):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    cn_charaters = pattern.findall(text)
    return collections.Counter(cn_charaters).most_common(count)


def main():
    data = load_file()
    text = merge_poems(data)
    print(stats_text_cn(text, 99))

if __name__ == '__main__':
 main()