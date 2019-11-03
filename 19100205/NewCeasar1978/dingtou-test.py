from mymodule.Think_Python_modules import make_wordlist
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

def draw_priceplot(filename):
    '''通过包含月度价格信息的文件，绘制价格曲线图。
    filename：文件名。
    '''
    with open(filename) as f:
        word_list = make_wordlist(filename)
        price_list = []
        for word in word_list:
            n = float(word)
            price_list.append(n)
    month_list = []
    for i in range(1,len(price_list)+1):
        month_list.append(i)

    #以下程序根据两个分别代表 x 和 y 轴的列表来绘制坐标曲线，注意在上方需要 import 的三个库
    T = np.array(month_list)
    power = np.array(price_list)


    xnew = np.linspace(T.min(),T.max(),300) #300 represents number of points to make between T.min and T.max
    power_smooth = spline(T,power,xnew)
    plt.plot(xnew,power_smooth)
    plt.show()

draw_priceplot('单边上涨价格走势.txt')