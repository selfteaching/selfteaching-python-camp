
# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()

# 找到所有好友
my_friend = bot.friends()
#搜索名称包含 'wxpy'，且成员中包含 `游否` 的群聊对象
#wxpy_groups = bot.groups().search('wxpy', [youfou])

# 监听好友信息，自动响应分享类型的消息
@bot.register(my_friend,SHARING)   

def get_friend_url(msg) :
    if isinstance(msg.type,SHARING):
        import requests # 使用 requests 请求文章的链接，获取返回结果（response）
        response = requests.get(msg.url)

        from pyquery import PyQuery # 提取微信正⽂
        document = PyQuery(response.text)
        content = document('#js_content').text()

        from mymodule import stats_word # 使用 stats_word 中的 stats_text 对提取结果进行分析和词频统计处理（返回前100个词的统计结果），将结果转换成 str 类型  
        result = str(stats_word.stats_text(content,100))
        
        msg.reply(result)
        

# 进入 Python 命令行、让程序保持运行
embed() 




