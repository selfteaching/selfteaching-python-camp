import mymodule.stats_word
import json
path = r'D:\用户目录\selfteaching-python-camp\exercises\1901040039\d10\tang300.json'
with open(path,'r', encoding='UTF-8') as f:
    #不加'r', encoding='UTF-8'会报UnicodeDecodeError
    read_date = f.read()
f.closed

try:
    print('前20的词频数：\n',mymodule.stats_word.stats_text_cn(read_date,20))
except ValueError as w:
    print(w)