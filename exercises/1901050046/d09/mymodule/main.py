#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import stats_word
import json

with open('tang300.json','r',encoding = 'utf-8') as f:
    load_dict = json.loads(f.read()) #打开json文件
text = ''
for i in range(0,len(load_dict)):
    text = text + (load_dict[i]['contents']+load_dict[i]['author']
    +load_dict[i]['title']+load_dict[i]['type'])+"\n" #提取汉字内容
print(stats_word.stats_text(text,100))#输出统计结果




