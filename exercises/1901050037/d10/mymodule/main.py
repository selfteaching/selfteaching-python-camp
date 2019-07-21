
# coding: utf-8

# In[18]:


import sys
sys.path.append(r'C:\Users\hx\Documents\GitHub\selfteaching-python-camp\exercises\1901050037\d10\mymodule')
import stats_word
from collections import Counter
import re
import json
import jieba

file_path = r"C:\Users\hx\Documents\GitHub\selfteaching-python-camp\exercises\1901050037\d10\mymodule\tang300.json"
word_lst1 = []
word_lst2 = []
word_lst3 = []
word_lst4 = []
with open(file_path, 'r', encoding='utf-8') as f:
    temp = json.load(f)
    for t in temp:
        contents_text=t["contents"].replace('［','').replace('］','').replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','').replace(' ','') #去掉特殊符号
        word_lst1.append(contents_text)
        text_cn1= "".join(word_lst1)
        
        type_text=t["type"].replace('［','').replace('］','').replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','').replace(' ','') #去掉特殊符号
        word_lst2.append(type_text)
        text_cn2= "".join(word_lst2)  
        
        author_text=t["author"].replace('［','').replace('］','').replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','').replace(' ','') #去掉特殊符号
        word_lst3.append(author_text)
        text_cn3= "".join(word_lst3)
        
        title_text=t["title"].replace('［','').replace('］','').replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','').replace(' ','') #去掉特殊符号
        word_lst4.append(title_text)
        text_cn4= "".join(word_lst4)
        
        
        text=text_cn2+text_cn1+text_cn4+text_cn3
#     print(contents_text)

stats_word.stats_text_cn(text,20)

