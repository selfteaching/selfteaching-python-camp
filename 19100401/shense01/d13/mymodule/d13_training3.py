import requests
from pyquery import PyQuery
import re
import jieba
from collections import Counter
from wxpy import Bot,Message,embed   #导入模块
import matplotlib.pyplot as plt
import numpy as np
# -*- coding: utf-8 -*-
 
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   # 雅黑字体
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['STHeiti'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题




bot = Bot()
my_friend = bot.friends() 
@bot.register(my_friend,'Sharing') 

def print_others(msg):
    if msg.type == 'Sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('p').text()
        content = re.sub('[a-zA-Z0-9’!"%&\'^\s+|\s+$()*+,-./:;，。?、…？“”‘’！]+',"",content)
        seg_list = jieba.cut(content, cut_all=True)
        result = Counter()
        for seg in seg_list:
                if len(seg) > 1:
                    result[seg] = result[seg] + 1
        mydic = result.most_common(20)
        source_data={}
        for i in mydic:
            source_data[i[0]] = i[1]
        print(source_data)

        # Set x y axis
        x_axis = tuple(source_data.keys())
        y_axis = tuple(source_data.values())
        plt.bar(x_axis, y_axis,width=0.5) 
        plt.xlabel(u"高频词汇")  # 指定x轴描述信息
        plt.ylabel(u"频次")  # 指定y轴描述信息
        plt.title("高频词汇统计表")  # 指定图表描述信息
        plt.ylim(0, int(y_axis[0]))  # 指定Y轴的高度
        plt.savefig('my_result.png')  # 保存为图片   
        msg.sender.send_image('my_result.png') 
        plt.show()   

embed() 
