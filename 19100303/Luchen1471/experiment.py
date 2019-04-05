#把d11练习里面的功能，先定义一个函数出来
import requests
from mymodule import stats_word
from pyquery import PyQuery
#def dealwiththemsg(msg0):    
#    response = requests.get(msg0.url)
#    document = PyQuery(response.text)
#    content = document('#js_content').text()
#    str_con = str(content)
#    return str(stats_word.stats_text_cn(str_con))
#    print(str(stats_word.stats_text_cn(str_con)))

#d11内容提炼
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
str_con = str(content)
#str_result = str(stats_word.stats_text_cn(str_con))
#print(str_result)
data_list = stats_word.stats_text_cn(str_con)
#print(data,type(data))
#列表换字典，但是i[0]和i[1]是什么意思没明白
data_dic = {}
for i in data_list:
    data_dic[i[0]] = i[1]
#print(data_dic)
#画图
#https://matplotlib.org/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

group_data = list(data_dic.values())
group_names = list(data_dic.keys())
group_mean = np.mean(group_data)
fig, ax = plt.subplots()
plt.rcParams['font.sans-serif']=['SimHei']#改中文字体
ax.barh(group_names, group_data)
#print(plt.style.available)
#plt.style.use('fivethirtyeight')
print(type(ax.barh(group_names, group_data)))
plt.show()


