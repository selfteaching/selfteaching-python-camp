from inspect import signature
from functools import wraps
import re,collections




import re
import os
from collections import Counter

 
def get_words_en(file):
    with open (file,'r', encoding='UTF-8') as f:
        words_box=[]
        for line in f:                         
            if re.match(r'[a-zA-Z0-9]*',line):#避免中文影响
                words_box.extend(line.strip().split())               
    user_counter = collections.Counter(words_box)
    print(user_counter.most_common(100))


def get_words_cn(file):
    with open (file,'r', encoding='UTF-8') as f:
        words_box=[]
        for line in f:                         
            if re.match(u'[\u4e00-\u9fff]+',line):#避免英文影响
                words_box.extend(line.strip().split())               
    user_counter = collections.Counter(words_box)
    print(user_counter.most_common(100))


def stats_text():
    #假设要读取文件名为aa，位于当前路径
    filename = 'd09/tang300.json'
    dirname = os.getcwd()
    fname = os.path.join(dirname, filename)
    
    get_words_en(fname)
    #get_words_cn(fname)

  







