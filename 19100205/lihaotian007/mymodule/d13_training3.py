import matplotlib.pyplot as plt
import numpy as np
import random as rd

def map_making(list_a) :
        """函数对导入的list结构处理，生成词频直方图，并保存到本地，返回保存的连接
        
        注意保存图片的地址连接可能需要修改
        """
        
        word = []
        number = []
        path = ''
        np.random.seed(19680801)
        plt.rcdefaults()
        fig, ax = plt.subplots()

        # 将导入的list拆分为两个list结构
        for i in range(len(list_a)) :
                word.append(list_a[i][0])
        for i in range(len(list_a)) :
                        number.append(list_a[i][1])

        # 定义图表数据
        word_map = np.array(word)
        y_pos = np.arange(len(word))
        number_map = np.array(number)
        error = np.random.rand(len(word))

        plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签

        # 生成图表
        ax.barh(y_pos, number_map, xerr=error, align='center',
                color='green', ecolor='black') 
        ax.set_yticks(y_pos)
        ax.set_yticklabels(word)
        ax.invert_yaxis()  
        ax.set_xlabel('number_map')
        ax.set_title('The word frequency statistics of this article')

        # 将图表保存到本地
        path = 'C:\\Users\\htLi0\Desktop\\picture\\' + str(rd.randint(1,100)) + '.png'
        print(path)
        plt.savefig(path)

        return path

# list_b = [('李',1),('浩',2),('天',3)]
# map_making(list_b)