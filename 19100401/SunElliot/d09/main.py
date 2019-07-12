from os import path
import collections
import json
import re


def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')
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

if  __name__ == '__main__':
    main()