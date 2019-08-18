# 先导入第三方库
import yagmail, requests, pyquery, getpass, csv
from pyquery import PyQuery
from  mymodule import stats_word
import matplotlib.pyplot as plt
import numpy as np
#提取正文
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') #获取该网页内容
document = PyQuery(response.text) 
content = document('#js_content').text() #将网页内容转换成文本

#分词统计
word_list = stats_word.stats_text_cn(content, 10)
word_dict = dict(word_list) 
data = []    
#遍历字典
for key, value in word_dict.items():                    #遍历字典
    temp = [value, key]                              #变量，变量值
    data.append(temp)                               #添加数据

#绘制直方图（词频TOP1-10）
plt.rcParams['font.sans-serif']=['SimHei']      #直方图正常显示中文字体
for i in range(0, 10):
    plt.bar((data[i][1],),(data[i][0],), facecolor='#9999ff', edgecolor='white')
plt.title('中文词频(TOP1-10)')  #显示标题
plt.xlabel('单词')                                   # 显示x轴名称
plt.ylabel('词频')                                   # 显示y轴名称
#plt.legend('直方图')                             #显示图例
plt.savefig('word_dict.png', dpi=300)
plt.show()                                            #显示作图结果

