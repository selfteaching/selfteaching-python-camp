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