import sys
import stats_word
from collections import Counter
import re

from os import path
import json

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