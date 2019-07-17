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
    entext2=""              
    for i in stri:
     if u'\u4e00' <= i <= u'\u9fa5':                    
         entext2+=i
    #cnt=Counter()
    count=20
    #for i in entext2:  
        #cnt[i]+=1  
    
    #筛选长度大于2的汉字：
    seg_list=jieba.cut(entext2,cut_all=False,HMM=False)
    poem_string = "/".join(seg_list)
    poem_string = poem_string.split("/")
    for i in poem_string:
      if len(i) >= 2:
         dictionary[i] = poem_string.count(i)
    dictionary = collections.Counter(dictionary).most_common(count)
    print(stats_text_cn. __doc__) 
    print(dictionary)


def main():
    location = sys.argv[0] #获取main.py的路径
    location = location.rstrip('main.py') + 'tang300.json' #获取tang300.json的路径

    with open(location,'r',encoding='UTF-8') as tang_text: #读取文件
        text = json.load(tang_text) #json转码
        text_all='' #初始化contents的容器
        for i in range(len(text)): #往容器里填contents
            text_all+=text[i]['contents'] #得到一个由contents组成的字符串


    stats_text_cn(text_all)


if __name__ == '__main__':
        main()
 