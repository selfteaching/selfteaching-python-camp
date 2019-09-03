from mymodule import stats_word

# file = open('/Users/Justco/selfteaching-python-camp/exercises/1901090003/d09/tang300.json','rb')
# text1 = file.read()
# text = text1.decode()

# print(stats_word.stats_text_cn(text,20))

# file.close()

#导入wxpy模块，定义是好友中的SHARING类型
from wxpy import *
bot = Bot()
my_friend = bot.friends()
@bot.register(my_friend,SHARING)

def auto_reply(msg):

#使⽤requests请求信息中的url
    import requests
    response = requests.get(msg.url)

#将response.text用pyquery把链接中内容提取出来
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text()

#使⽤用stats_word中的stats_text对提取结果进⾏行行分析和词频统计处理理(返回前100个词的 统计结果)
    result = str(stats_word.stats_text_cn(content,100))
    print(result)
    msg.reply(result)      #msg.reply是自动回复?
    
embed()   #保持后台运行



#通过yagmail登录⾃自⼰己的邮箱，将统计结果发送邮件
# import yagmail
# user = input('账号:')
# password = input('密码:')
# smp = 'smtp.qq.com'
# yagmail.SMTP(user=user,password=password,host=smp).send('pythoncamp@163.com', '【1901090003】自学训练营 DAY11 minidv963', str(stats_word.stats_text_cn(content,100)))


