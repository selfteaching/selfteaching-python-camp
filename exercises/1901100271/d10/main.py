from mymodule import stats_word
from os import path
import json
import logging
import jieba


logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)


def load_file():
    '''
    1·
    下面是常用的获取文件路径的方式，要确保tang300.json跟当前文件在同一文件夹下，这两种方式都可以用，等价
    '''
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
    '''
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
    2·
    当要获取的文件tang300.json在当前文件的上一级目录中时使用
    file_path = path.join(path.dirname(path.abspath(__file__)), '../data/tang300.json')
    3·
    当要获取的文件tang300.json在当前文件上一级目录的某个文件夹data下时使用
    file_path = path.join(path.dirname(path.abspath(__file__)), '../data/tang300.json')
    '''
    print('当前文件路径:', __file__, '\n读取文件路径:', file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


'''
有了上面获取文件路径的方法，就不用每次都这样子去输入文件路径了。
with open("C:\\Users\\noodl\\Desktop\\Github\\selfteaching-python-camp\\exercises\\1901100271\\d09\\tang300.json", encoding='UTF-8') as f:
    data = f.read()
'''


def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    seg_list = jieba.cut(poems, cut_all=False)
    return seg_list


def main():
    try:
        data = load_file()
        logging.info(data[0])
        poems = merge_poems(json.loads(data))
        print(poems)
        logging.info('result ==> %s', stats_word.stats_text_cn(poems, 20))
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
