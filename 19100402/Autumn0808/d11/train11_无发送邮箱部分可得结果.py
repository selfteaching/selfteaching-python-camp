#导入所需模块
import requests
from pyquery import PyQuery
from mymodule import stats_word
import yagmail
import getpass

#通过URL获取公众号文章
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#获取公众号正文文本
document = PyQuery(response.text)
content = document('#js_content').text()

#对文本进行词频统计，输出前100的结果，并转换成字符串类型
statsList = stats_word.stats_text(content,100)
statsString = ''.join(str(i)for i in statsList)

print(statsString)