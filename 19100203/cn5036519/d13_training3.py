import matplotlib.pyplot as plt
import numpy as np
import d11_training1
from matplotlib.font_manager import FontProperties


font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf",size=10)


def generate_charts(url):
        # 当设置相同的seed，每次生成的随机数相同。
        np.random.seed(19680801)

        #重置rc所有参数，类似初始化
        plt.rcdefaults()
        #建立一个子图对象
        fig, ax = plt.subplots()
        #获取排列在前的10个词频
        words_list = []
        counts_list = []
        for el in d11_training1.get_request(url):
                words_list.append(el[0])
                counts_list.append(el[1])
        # y_pos 赋值为[0 1 2 3 4], len(people)求元素数量为5，
        y_pos = np.arange(len(words_list))

        performance = counts_list
        error = np.random.rand(len(words_list))

        # 生成一个水平的条形图，y_pos为y轴的坐标,performance 是条的宽度
        ax.barh(y_pos, performance, xerr=error, align='center',
                color='green', ecolor='black')
        #设置 y 轴的命名位置，需要跟下面的 set_yticklabels 配合使用
        ax.set_yticks(y_pos)
        #设置 y 轴的标签名称
        ax.set_yticklabels(words_list, fontproperties = font)
        # 反转 y 轴
        ax.invert_yaxis()  
        # x 轴的标题
        ax.set_xlabel('词频数', fontproperties = font)
        #整个图的标题
        ax.set_title('网页词频统计概况', fontproperties = font)
        #显示此图表
        # plt.show()
        # 保存图表
        plt.savefig('./tupian.jpg')



