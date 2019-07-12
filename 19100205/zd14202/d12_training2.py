from wxpy import *
bot = Bot() # 导入wxpy库，通过手机扫码登录微信
my_friend = bot.friends() # 徐悦学长的方法，将my_friend定义为所有好友
@bot.register(my_friend,SHARING) # 这个函数装饰器以及下面的auto_play函数是徐悦学长的方法。经分析，装饰器的作用是监听来自my_friend的消息，如果类型为SHARING（分享内容），即把消息内容赋值给msg变量
def auto(msg):
    text = msg.url
    print(text)
    #以下为第11天作业内容，注意缩进！这部分内容必须包含在以上的auto_play函数定义部分
    import requests
    import pyquery
    from pyquery import PyQuery
    from mymodule import stats_word

    #'''访问网址'''
    image_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
    #'''将网址中的内容全部赋值给response'''
    response = requests.get(image_url)
    #'''提取网址中的正文内容'''
    document = pyquery.PyQuery(response.text) #抓取文字信息
    content = document('#js_content').text() #把抓取的内容写成可视的文字
    #以上为第11天作业内容
    return str_1 # 这里函数返回的结果将直接自动回复给发送消息的好友（my_friend），这应该就是auto_reply这个函数的作用，但为什么这明明是个自己定义的函数，却能自带自动回复的功能？
embed() # 保持监听状态，如果没有，程序运行到此处就会结束