from wxpy import *
import stats_word
import requests
from pyquery import PyQuery

def main():
    # 初始化机器人，扫码登陆
    bot = Bot()
    # 搜索好友
    my_friend = bot.friends()
    # 回复 my_friend 的消息 (优先匹配后注册的函数!)
    @bot.register(my_friend,SHARING)
    
    def auto_accept_friends(msg):
        response = requests.get(msg.url) 
        document = PyQuery(response.text)
        content = document('#js_content').text()
        result = stats_word.stats_text_cn(content)
        return result
    
    # 进入 Python 命令行、让程序保持运行
    embed()
if __name__ == '__main__':
    main()