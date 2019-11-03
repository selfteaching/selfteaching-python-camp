import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA', auth=('user', 'pass'))
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()
from mymodule.stats_word import stats_text_3 as f
result = f(content)
print(result)
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
word = []
frequency = []
for i in result:
    word.append(i[0])
    frequency.append(i[1])
y_pos = np.arange(len(word))
#performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(word))
plt.rcParams['font.sans-serif'] = ['SimHei']
ax.barh(y_pos, frequency, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(word)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('词语')
ax.set_title('词频统计结果')

plt.show()


text='''import yagmail
username = input('输入发送邮箱用户名：')
passport = input('输入发送邮箱密码：')
recipient = input('请输入接收者邮箱：')
yag = yagmail.SMTP(username,passport,host='smtp.qq.com')
yag.send(recipient,"词频统计",result)'''

