from wxpy import *
bot = Bot() # 导入wxpy库，通过手机扫码登录微信
my_friend = bot.friends() # 徐悦学长的方法，将my_friend定义为所有好友
@bot.register(my_friend,SHARING) # 这个函数装饰器以及下面的auto_play函数是徐悦学长的方法。经分析，装饰器的作用是监听来自my_friend的消息，如果类型为SHARING（分享内容），即把消息内容赋值给msg变量
def auto_reply(msg):
    text = msg.url
    print(text)
    #以下为第11天作业内容，注意缩进！这部分内容必须包含在以上的auto_play函数定义部分
    import requests
    response = requests.get(text) # 通过requests请求文章链接，获取网页内容


    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text() # 将网页内容提取为一个字符串文本作为输入

    print(content)


    import mymodule.stats_word
    try:
        if not isinstance(content,str):
            raise ValueError()
        
    except ValueError:
        print('输入的不是文本格式，请重新输入：')   
    dic = mymodule.stats_word.stats_text_cn(content) # 调用函数进行分词并统计词频
    str_1 = str(dic) # 将词频统计结果（字典形式）转换成字符串
   
    #以上为第11天作业内容
    return str_1 # 这里函数返回的结果将直接自动回复给发送消息的好友（my_friend），这应该就是auto_reply这个函数的作用，但为什么这明明是个自己定义的函数，却能自带自动回复的功能？

embed() # 保持监听状态，如果没有，程序运行到此处就会结束
