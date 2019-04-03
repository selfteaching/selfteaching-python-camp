# 导入模块
from wxpy import * 
import requests
from pyquery import PyQuery

# 初始化机器人，扫码登陆

bot = Bot()

# 搜索名称含有 " " 的好友
my_friend = bot.friends()

# 发送文本给好友
#my_friend.send('Hello WeChat!')

# 发送图片
#my_friend.send_image('my_picture.jpg')

#
@bot.register([Groups,Friend], SHARING, except_self = False)
#def word_frequency(meg) :
def print_others(msg):
    print(msg)
    response = requests.get(msg.url) #提取公众号伪代码
    document = PyQuery(response.text)
    content = document('#js_content').text() #把抓取的内容写成可视的文字
    #print(content)
    import  stats_word
    #统计内容的前100词频
    statlist = stats_word.stats_text_cn(content,100)
    statString = "".join(str(i) for i in statlist)
    return statString
    #print(statlist)
embed()# 进入 Python 命令行、让程序保持运行
