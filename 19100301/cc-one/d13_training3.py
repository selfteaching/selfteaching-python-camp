#2019.04.05 cc-one 倒数第二次作业 还差一天结束
#matplotlib的例程倒是能看懂，简简单单的几行，随便就可以复制过来
#跟前几天的程序匹配上这次没有报错
#对于返回结果好像有点问题，在issue里面没看到类似的提问
#现在每天都会翻阅前几期毕业的学生的优秀例程，发现差距蛮大的，有人用简单的几行，代码优美，就能解决问题
#有人代码冗余，解决的问题的路径比较复杂，但是最终也是解决了


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontManager, FontProperties
#from pylab import *

#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

cnfont = FontProperties(fname='/Users/candicebabybeet/Library/Fonts/SourceHanSans-Bold.otf')
'''
font.family : sans-serif
font.sans-serif : SimHei, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
axes.unicode_minus:False

from matplotlib.font_manager import_rebuild
_rebuild()
'''

def creat_chart(x, y):

    plt.rcdefaults()
    fig, ax = plt.subplots()

    #输入data
    people = x
    y_pos = np.arange(len(people))
    performance = np.array(y)
    #error = np.random.rand(len(people))

    ax.barh(y_pos, performance, align='center',color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people,fontproperties = cnfont,color='green')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词语列表',fontproperties = cnfont,color='green')
    ax.set_title('统计表格',fontproperties = cnfont,color='green')
    #plt.show()

    return plt.savefig('chart.jpg')

'''
x = ['牛儿', 2, 3]
y = [3, 3, 1]

print(creat_chart(x, y))

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
'''