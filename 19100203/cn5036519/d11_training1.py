import requests, yagmail, getpass
from pyquery import PyQuery
from mymodule import stats_word


# # day11作业
# # 通过get请求获取响应数据
# response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
# # 从响应数据中提取正文内容
# document = PyQuery(response.text)
# content = document('#js_content').text()
# # 邮件内容定义
# content1 = '''Dear Coach Zhang:
#     hello, the statistics of today's homework are as follows:\n\n'''
# content2 = str(stats_word.stats_text_cn_v3(content, 10))
# # 邮件发送
# sender = input("请输入发件人邮箱：")
# password = getpass.getpass("请输入发件人邮箱密码：")
# recipients = input("请输入收件人邮箱：")
# yag = yagmail.SMTP(user=sender, password=password, host='smtp.126.com')
# yag.send(recipients, '19100203 cn5036519', content1+content2)


# day12作业
# 把上面的代码封装成一个函数
def get_request(url):
    response = requests.get(url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    return stats_word.stats_text_cn_v3(content, 10)
