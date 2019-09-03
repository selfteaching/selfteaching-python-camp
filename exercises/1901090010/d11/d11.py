import requests
from pyquery import PyQuery
from mymodule import stats_word_d11 as swd11
import yagmail
#使用 requests 请求 参考资料4 微信公众号文章的链接，获取返回结果（response）
#将 response.text 用 pyquery 把微信公众号正文提取出来
response  = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
# print(response.text)    #可以查看显示数据，或者隐藏


# 提取微信公众号正文伪代码示例
document = PyQuery(response.text)
content = document('#js_content').text()
# print('content =', content)    #可以查看显示数据，或者隐藏

#使用stats_word 中的 stats_text 对提取结果进行分析和词频统计处理（返回前 100 个词的统计结果），将结果转换成 str 类型
result = swd11.stats_text_cn(content,100)
result=str(result)
# print(result)      #可以查看显示数据，或者隐藏

#登陆自己的邮箱
user_name = input('请输入发件人邮箱：')
password = input('请输入发件人邮箱密码，注意是授权码：')
yag = yagmail.SMTP(user=user_name, password=password,host='smtp.qq.com')

#发送邮件，登录邮箱查看是否发送成功
yag.send(to = 'pythoncamp@163.com', subject='[title：【1901090010】自学营008期01班day11+Mary]', contents = result)
print("发送成功")
