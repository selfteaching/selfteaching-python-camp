# 安装第三方库  requests ,yagmail,pyquery
# request  获取网页内容
# yagmail  发送邮件
# pyquery  获取text
import requests
import yagmail
from pyquery import PyQuery as py
import mymodule.stats_word as sw
import getpass

r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")#获取网页数据
web_text =r.text#使用变量web_text保护网页文本数据(这时会保存很多js代码以及其他function的代码,并不是里面所有的东西是我们需要的)
document=py(web_text)
content =document('#js_content').text()#js_content 是网页主文内容的div ,id为js_content,以后我们爬不同的数据,需要去看一下别人家的网页代码

# print(content)#测试看一下得回来的数据是什么
result =sw.stats_text_cn(content,100,False)
result=str(result)
# print(isinstance(result,str))#显示数据

sender = input("请输入您的发件人邮箱")
password =  getpass.getpass("输入发件人邮箱密码")


yagmail.register(sender, password)
yag =yagmail.SMTP(sender,password,'smtp.qq.com')
yag.send('pythoncamp@163.com', '19100103 lucasLu0724', result)
print("发送成功")