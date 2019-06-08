'''这是一个将数据可视化后，把结果发给用户的程序'''

import matplotlib.pyplot as plt
import numpy as np


def Horizontal_bar_chart(data):
    '''修复随机状态'''
    np.random.seed(19680801)

    '''不知道在干什么，好像是定义变量'''
    plt.rcdefaults()
    fig, ax = plt.subplots()

    '''处理数据'''
    words = (data[0])
    y_pos = np.arange(len(words))
    number = 3 + 10* np.random.rand(len(words))
    error = np.random.rand(len(words))

    '''设置图表样式'''
    ax.barh(y_pos,number,xerr = error,align = 'center',color = 'bule',ecolor = 'black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    ax.set_xlabel('出现次数')
    ax.set_title('关于您发给我分享文章中的中文词频统计图表')
    
    return plt.show()
