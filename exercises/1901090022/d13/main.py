from mymodule import stats_word
import requests
from pyquery import PyQuery
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

def draw_bar_chart(title, yticklabels, ytickvalues):
    """ 生成水平柱状图
    """
    font_properties = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
    plt.rcParams['font.sans-serif'] = ['PingFang'] #用来正常显示中文标签 
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

    plt.rcdefaults()
    fig, ax = plt.subplots()

    y_pos = np.arange(len(yticklabels))
    ax.barh(y_pos, ytickvalues, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(yticklabels, fontproperties=font_properties)
    ax.invert_yaxis()  # 根据每项的数值升序，从上至下排列显示
    ax.set_xlabel('词频统计', fontproperties=font_properties)
    ax.set_title(title, fontproperties=font_properties)

    plt.show()

r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")

document = PyQuery(r.text)
content = document('#js_content').text()
doc_title = document('#activity-name').text()

word_list = stats_word.stats_text_cn(content, 20)
print(word_list)

yticklabels = []
ytickvalues = []
for x in word_list:
    yticklabels.append(x[0])
    ytickvalues.append(x[1])

draw_bar_chart(doc_title, yticklabels, ytickvalues)

