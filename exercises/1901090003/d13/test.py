from mymodule import stats_word
import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#将response.text用pyquery把链接中内容提取出来
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()

#使⽤用stats_word中的stats_text对提取结果进⾏行行分析和词频统计处理理(返回前100个词的 统计结果)
result = str(stats_word.stats_text_cn(content,20))

#开始制作图表部分
#import matplotlib.pyplot as plt
import numpy as np
#解决MAC无法正常显示问题  
import matplotlib  
import matplotlib.pyplot as plt
from pylab import mpl

# plt.rcParams['font.family'] = ['Light'] #正常显示中文 
# plt.rcParams['font.sans-serif'] = ['STFangsong']
# plt.rcParams['font.sans-serif'] = ['STFangsong']
# plt.rcParams['font.sans-serif'] = ['simhei']
# mpl.font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
# plt.rcParams['font.family'] = ['Arial Unicode MS'] #正常显示中文
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['font.family'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] =  False
fig, ax = plt.subplots()
result_list=eval(result)
word=[]
number=[]
for i in result_list:
    word.append(i[0])
    number.append(i[1])

word = tuple(word)
y_pos = np.arange(len(word))
number = np.array(number)
error=np.random.rand(len(word))

#plt.rcParams['font.sans-serif'] = ['SimHei']         #将中文字体显现
ax.barh(y_pos,number,xerr=error,align='center',color='red',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(word)

ax.invert_yaxis()
ax.set_xlabel('出现次数') 
ax.set_title('词频统计表')

plt.savefig('day13.jpg')
plt.show()