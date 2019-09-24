
import requests
import pyquery                                                          # PyQuery库是网页解析库，是Python仿照jQuery的严格实现，语法与jQuery几乎完全相同

# 第一步：请求微信文章的链接，获取返回结果response(r)
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')   # 向网页提交get请求，得到一个requests对象r。
print(r.text)                                                           # r.text是请求网页后返回的内容。text属性是针对相应内容是文本（如HTML等）的情况下使用

# 第二步：用pyquery提取微信文章正文内容
document = pyquery.PyQuery(r.text)                                      # 通过pyquery获取文档，这里是获取一个网页，或解析一个网页的意思。
content = document('#js_content').text()                                # '#js_content'是网页的一个标签名，这个标签中存放着文档的内容。
print (content)                                                         # 打印出要提取的微信文章内容

# 笔记
# 除了上面代码外，还可以使用以下代码提取微信公众号正文伪代码：
# import requests
# from pyquery import PyQuery
# r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
# document = PyQuery(r.text)
# content = document('#js_content').text()
# print(content)


# 第三步：调用stats_word中的stats_text函数以统计中文汉字词频前100个，并将结果转为str类型
from mymodule.stats_word import stats_text     # 从 模块中(mymodule是包，stats_word是模块) 导入 函数stats_text
text=content                                  # 将content赋值给text
print(stats_text(text,100))                   # 打印出前100个词的统计结果（Counter对象是dict的子类）
dict_result = stats_text(text,100)            # 把结果赋值给dict_result
print(str(dict_result))                       # str()函数将某一类型的变量或者常量转换为字符串

# 笔记
# 用以下代码测试，得出结果为<class 'str'>
# res = str(dict_result)
# print(type(res))

# 第四步：通过yagmail登录自己的邮箱，将统计结果发送到指定邮箱

# 实现邮箱和密码的输入，以保护自己的邮件和密码
import getpass
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴)：')  # 运行后，在terminal命令行复制后敲回车即可。注意为了保护密码输入，复制的授权码是不会在命令行显示的。
recipients = input('输入收件人邮箱：')

# 实现分词统计和发送邮件
import yagmail     
yag = yagmail.SMTP(sender, password,'smtp.qq.com')         # 链接服务器，此处的password为邮箱的授权码，不是邮箱登录密码 
to = recipients                                            # 收件人邮箱地址
subject = '自学训练营学习9群 Day11 AmazingJulie'             # subject为邮件标题
contents = str(dict_result)                                 # contents 为邮件内容
yag.send(to, subject, contents)                             # 执行发送邮件命令