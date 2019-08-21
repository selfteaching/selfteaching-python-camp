
#导入wxpy 模块
from wxpy import Bot,Message,embed

bot = Bot() #初始化机器人，扫码登录

my_friend = bot.friends().search('someone')[0] #搜索名称含有‘somebody’的微信好友
my_friend.send('Hello, please send me a message.')#给微信好友发送信息

@bot.register(my_friend) #装饰器，匹配好友，空默认匹配所有
def auto_reply(msg):
    '''This function aims to gain the url from weichat message

    and to reply  words frequency of Sharing Chinese articels.'''

    if msg.type == 'Sharing': #只处理类型为Sharing的信息
        url = msg.url
        from mymodule import stats_word
        import requests
        response = requests.get(url)

        #提取文章正文
        from pyquery import PyQuery
        document = PyQuery(response.text)
        content = document('#js_content').text()
    
        #统计文章汉语词频
        output = stats_word.stats_text_cn(content,10)

        #制作图表
        k = list(output.values())
        g = list(output.keys())
                
        import matplotlib.pyplot as plt
        import pandas as pd

        s = pd.Series(k,index = g)
            
        plt.rcParams['font.sans-serif']=['SimHei'] #让图片能够显示汉字
        plt.subplots()
        s.plot(kind='bar',color = 'red',grid = True,alpha = 0.5)

        plt.savefig('词频统计.png')#保存图片

        msg.sender.send_image('词频统计.png')#将图片发送给好友

embed() #进入Python 命令，让程序保持运行