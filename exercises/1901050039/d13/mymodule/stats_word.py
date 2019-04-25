
import re
import jieba
from collections import Counter  #引入counter模块，数数
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# #定义函数
def stats_text_cn(text):
    """This is for the article written in Chinese
    """
    if type(text) != str:
        raise ValueError('This is a wrong type')
    else:
        text = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", text)
        t1 = text.replace(" ","")

        #jieba分词
        seg_list = jieba.cut(t1,cut_all=False)
        res2 = Counter(seg_list).most_common(10)

        #制表
        res3 = dict(res2)
        x = tuple(res3.keys())
        y = tuple(res3.values())
        plt.bar(x,y,width=0.5)
        plt.title("高频词汇表")
        plt.xlabel("高频词汇")
        plt.ylabel("次数")
        plt.savefig('list.png')
        plt.show()
        print('process img done')
        return 'list.png'
    
      

