import numpy as np
from mymodule import stats_word
from pyquery import PyQuery as py
import requests
import matplotlib.pyplot as plt

reponse = requests.get('https://mp.weixin.qq.com/s/_oFklhozwgz_1QnB_pLioA')   # 网页请求
web_text = reponse.text    # 保存更多网页文本数据
document = py(web_text)
content = document('#js_content').text()

w_list = stats_word.stats_text_cn(content, 10)
w_list = dict(w_list)
# group_data = list(w_list.values())
group_data = tuple(w_list.values())
group_names = list(w_list.keys())
# plt.rcdefaults()
fig, ax = plt.subplots()  # 建立一个figure对象，建立一个axis对象
y_pos = np.arange(len(group_names))
ax.barh(y_pos, group_data, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(group_names)
ax.invert_yaxis()
ax.set_xlabel('词频')
ax.set_title('网页中TOP10中文词语')
plt.show()

# plt.savefig(r'wordsCnt.jpeg')  #保存图片
# msg.reply_image(r'wordsCnt.jpeg')  #回复图片
