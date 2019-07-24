from os import path
import collections
import json
import re
import jieba

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
    with open(file_path, 'rb') as f:
        return json.load(f)


def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems


def stats_text_cn(text, count):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    cn_charaters_list = pattern.findall(text)
    cn_charaters = ''.join(cn_charaters_list)
    cn_charaters = [x for x in jieba.cut(cn_charaters, cut_all=False) if len(x) >= 2]
    return collections.Counter(cn_charaters).most_common(count)


def main():
    data = load_file()
    text = merge_poems(data)
    print(stats_text_cn(text, 20))


if __name__ == '__main__':
    main()
