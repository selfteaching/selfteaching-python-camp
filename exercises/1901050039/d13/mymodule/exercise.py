import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# #定义函数
def wordtable(res):
        res2 = dict(res)
        x = tuple(res2.keys())
        y = tuple(res2.values())
        plt.bar(x,y,width=0.5)
        plt.title("高频词汇表")
        plt.xlabel("高频词汇")
        plt.ylabel("次数")
        plt.savefig('list.png')
        plt.show()
        return 'list.png'
    
      

