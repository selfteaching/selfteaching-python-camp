#引入邮箱库
import yagmail
#引入网络请求库
import requests 
#引入词频处理模块
import stats_word 
#引入密码输入模块
import getpass  
#从文档解析库中引入文档解析函数
from pyquery import PyQuery 

def task(): #创建任务函数
    #获取微信文章内容
    response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    document=PyQuery(response.text)
    content=document('#js_content').text()
    #采用stats_word模块中中文字符处理函数进行处理
    word=stats_word.stats_text_cn(content,count=100)
    #打印确认结果
    print(str(word))
    #登陆发送结果到邮箱
    sender=input("请输入你邮箱地址：")
    mima=getpass.getpass("请输入你的邮箱密码：")
    accepter=input("请输入收件人地址:")
    subject=input("请输入邮件标题")
    yag=yagmail.SMTP(sender,mima,'smtp.qq.com')
    yag.send(to=accepter,subject=subject,contents=str(word))
    
if __name__ == '__main__':
    task()