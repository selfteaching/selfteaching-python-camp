from mymodule import stats_word #读取模块
import json #引入jsan解码库
import jieba

import requests #引入requests库用于获取网页HTML信息

import pandas
import numpy as np
import matplotlib.pyplot as plt

from pyquery import PyQuery as pq #引入pyquery库解析获取的HTML信息

from matplotlib.font_manager import _rebuild
_rebuild()

with open('tang300.json',mode='r',encoding='utf-8') as f: #创建文件对象f，内容为打开并读取“唐诗300.json文件中的字节”
    read_data = f.read() #设定字符串read_data，其对应为文件f中的内容
something = stats_word.stats_text_cn(read_data,10)
plt.rcdefaults() #恢复到缺省的配置(matplotlib载入时从配置文件读入的配置)?
fig,ax = plt.subplots() #初始化，面向对象画图。在图表中创建子图fig.ax   fig画布 ax对象
plt.rcParams['font.sans-serif'] = ['STFangsong'] #ttc中字文件转不了ttf，先写着吧
plt.rcParams['axes.unicode_minus'] = False #ttc中字文件转不了ttf，先写着吧
dict_something = dict(something) #字典化了那个统计结果列表，应该直接可转吧
print(dict_something)
x_val = tuple(dict_something.keys())
y_val = tuple(dict_something.values())
y_pos = np.arange(len(x_val)) #y——pos的范围设定为0到xv的个数
error = np.random.rand(len(x_val)) #error为在len(x_val)范围内的随机数？
ax.barh(y_pos,y_val,xerr=error,align='center') #绘制一个width为y_pos即10,bottom为y_val的横向条形图，xerr=error是什么意思？align为设定子图居于有值的视窗中间
ax.set_yticks(y_pos) #设定y轴上的值个数，本案例为10（每个刻度线都是一个ytick对象）
ax.set_yticklabels(x_val) #设定y轴刻度标签设定为x_val内的数据，本案例即排在前10的10个词
ax.invert_yaxis() #y轴上的刻度标签倒过来排列 （官方说明：labels read top-to-bottom）
ax.set_xlabel('高频词') #设置y轴的标题
ax.set_ylabel('出现次数') #设置x轴的标题
ax.set_title('词频统计表') #设置图形的标题
plt.savefig("词频统计图.png") #把该图另存为“词频统计图。png”，分辨率为默认值



#以上函数没有使用return等结构我没太看懂，应该是@装饰器的使用与一般的函数不一样，得查询清楚



#本次作业由于微信改版的原因，wxpy库不能正常运行，一直报错'pass ticket'。所以以上代码是未经测试的，回头阅读完装饰器内容后，找机会回来做测试。