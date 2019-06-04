from os import path
import collections
import json
import re
'''导入jieba'''
import jieba

'''获取文件路径的方式，要确保 tang300.json 跟当前文件在同一文件夹下，这两种方式等价'''
def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')
    print('当前文件路径：', __file__,'\n读取文件路径：', file_path)

    '''读取唐诗300首'''
    with open(file_path) as f:
        return json.load(f)

'''定义merge_poems合并所有contents内容'''
def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems


def stats_text_cn(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    cn_characters = pattern.findall(text)
    return "".join(cn_characters)

'''jieba精确模式'''
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