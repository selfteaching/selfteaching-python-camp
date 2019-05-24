from collections import Counter
from os import path
import json

def stats_text(text):
    if type(text) != str:
        raise ValueError('非字符串类型')
    list_en = stats_text_en(text)
    list_cn = stats_text_cn(text)
    list_all = list_en+list_cn
    return list_all

def stats_text_en(text):
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())
    count_dict = {}
    for word in word_list:
        count_dict[word] = word_list.count(word)
    list_en = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    return list_en

def stats_text_cn(text):
    text_cn = re.sub(r'[\wa-zA-Z0-9]','',text)
    count_dict = {}
    for character in text_cn:
        count_dict[character] = text_cn.count(character)
    list_cn = sorted(count_dict.items(), key = lambda x:x[1], reverse=True)
    return list_cn

def load_file():
    file_path = path.join(path.dirname(path.abspath(__file__)),'tang300.json')
    with open(file_path,'r', encoding='utf-8') as file:
        return json.load(file)
    
s = load_file()
text = ''
for i in s:
    text +=str(i)

cnt = Counter()
for word in [text]:
    cnt[word] +=1
words100 = Counter(word).most_common(100)
print(words100)