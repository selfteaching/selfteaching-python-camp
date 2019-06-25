#2019.04.02 cc-one 
#jieba 的安装很简单，程序的调试一点都不简单

from os import path
import collections
import json
import re

import jieba

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
    print('当前文件路径：', __file__,'\n读取文件路径：', file_path)

    with open(file_path) as f:
        return json.load(f)

def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems


def stats_text_cn(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    cn_characters = pattern.findall(text)
    return "".join(cn_characters)


def cut_poems(list1):
    list2=[]
    seg_list = jieba.cut(list1, cut_all=False)
    for i in seg_list:
        if len(i)>=2:
            list2.append(i)
    return list2

def count(list3, count):
    return collections.Counter(list3).most_common(count)

def main():
    data = load_file()
    text = merge_poems(data)
    list1 = stats_text_cn(text)
    list3 = cut_poems(list1)
    print(count(list3, 20))


if __name__ == '__main__':
    main()