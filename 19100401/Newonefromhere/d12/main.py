#创建函数统计网页文章的汉语词频
def data_cn(sharing):
    
    '''This function aims to analyze Chinese words frequency.'''

    from mymodule import stats_word
    import requests
    response = requests.get(sharing)

    #提取文章正文
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text()
    
    #统计文章汉语词频
    output = stats_word.stats_text_cn(content,100)
    output_str = str(output)
    return output_str

#导入wxpy 模块
from wxpy import Bot,Message,embed

bot = Bot() #初始化机器人，扫码登录

my_friend = bot.friends().search('somebody')[0] #搜索名称含有‘somebody’的微信好友
my_friend.send('Hello, please send me a message.')#给微信好友发送信息

@bot.register(my_friend) #装饰器，匹配好友，空默认匹配所有
def auto_reply(msg):
    '''This function aims to gain the url from weichat message

    and to reply  words frequency of Sharing Chinese articels.'''

    if msg.type == 'Sharing': #只处理类型为Sharing的信息
        url = msg.url
        re_friend=data_cn(url)
        msg.reply(re_friend) #给好友返回结果
    else:
        print("Your friend doesn't send a message")

embed() #进入Python 命令，让程序保持运行