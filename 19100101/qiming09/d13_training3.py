# this is d13 excercise for 3rd-party library "matplotlib" and "numpy"
# date : 2019.3.30
# author by : qiming

import matplotlib.pyplot as plt 
import numpy as np 

# 定义绘制图标函数并保存为图片
def chartImg(data={}) :
    group_x = list(data.keys())
    group_y = list(data.values())
    fig, ax = plt.subplots()
    ax.barh(group_x, group_y, color='blue')
    ax.set(xlabel= 'Quantity', ylabel='Wrod', title='Word Frequency Statistics')
    plt.savefig('chart.png')
    return 'chart.png'