# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:24:06 2019

@author: PetalSaya
"""
import stats_word
import requests
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

document = PyQuery(response.text)
content = document('#js_content').text()

result = stats_word.stats_text_cn(content,10)

result_dict = {}
for i in result:
    result_dict[i[0]]=i[1]       
keys=tuple(result_dict.keys())
values=tuple(result_dict.values())

plt.rcdefaults()
fig,ax = plt.subplots() 
        
y_pos = np.arange(len(keys)) #y轴词的个数
        
        
ax.barh(y_pos,values,align='center',color='blue',ecolor='black')
        

ax.set_yticks(y_pos)
ax.set_yticklabels(keys,fontproperties="SimHei")
ax.invert_yaxis()
ax.set_xlabel(u'频率',fontproperties="SimHei")
ax.set_title(u'前10词频统计图',fontproperties="SimHei")
        
plt.show()