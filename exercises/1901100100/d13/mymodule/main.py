import requests
from pyquery import PyQuery as pq
import getpass
import stats_word
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.font_manager import *


myfont = FontProperties(fname='C:\Windows\Fonts\msyh.ttc')  #make the font of chinese 雅黑
#get the information of the web
url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
r = requests.get(url)
#get all the content of the web
document = pq(r.text)
content = document('#js_content').text()
#get the useful text by the pyquery way
#print(content)

try:
    dict1_order = stats_word.stats_text_cn(content,100)
    #get the order of the 100th number
    word_ar = np.array(dict1_order)
    #print(word_ar)
    word = word_ar[:,0]  #取统计集合的汉语词组作为一个列表
    index = word_ar[:,1]   #去统计集合中的词组出现次数作为列表
    print(word)
    print(index)
    #index = [float(i) for i in index]
    index = index.astype(float)    #将次数转换成浮点数
    y_pos = np.arange(len(word))
    plt.rcdefaults()
    fig,ax = plt.subplots(figsize=(10, len(index) * 0.8))
    ax.barh(y_pos,index,height= 0.8)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word, fontproperties=myfont)
    ax.invert_yaxis() 
    ax.set_xlabel('字数频度', fontproperties=myfont)
    ax.set_title('index of the word')
    fig.savefig('stats1.png')
    plt.show()

except ValueError as e:
    print("the text needed to be sorted is not a string, please try again!\n ",e)
    #this sentence is use to print the information of the exception


