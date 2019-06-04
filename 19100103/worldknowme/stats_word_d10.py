#-*- coding:utf-8 -*-
# -*- coding:gbk -*-
from os import path
import json
import re
import collections
import io
import sys
from collections import Counter               
import jieba
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def stats_text_cn(stri):  
    '''【注】:stats_text_cn()函数为每个汉字统计的次数如下： '''  
    if type(stri) != str:
     raise ValueError("This is not string!")
    dictionary={}                                      
    entext2=[]              
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    
         entext2.append(i)
    
    cnt=Counter()
    count=20
    for i in entext2:  
        cnt[i]+=1  
    
    #筛选长度大于2的汉字：
    seg_list=jieba.cut(entext2,cut_all=False,HMM=False)
    string = "/".join(seg_list)
    string = string.split("/")
    for i in string:
      if len(i) >= 2:
         dictionary[i] = string.count(i)
    dictionary = collections.Counter(dictionary).most_common(count)
    print(stats_text_cn. __doc__) 
    print(dictionary)
   


def load_file():              #路径下的tang300.json读不出来，脑袋疼......
    file_path = path.join(path.dirname(path.abspath(__file__)), 'tang300.json')  
    print('当前文件路径：', __file__, '\n读取文件路径：', file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)  

def merge_poems(data):
    poems = ''
    for item in data:
        poems += item.get('contents', '')
    return poems

def main():
    data = load_file()
    text = merge_poems(data)
    stats_text_cn(text)


if __name__ == '__main__':
 main()
 