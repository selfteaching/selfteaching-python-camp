from wxpy import Bot,Message,embed   #导入模块
import d12_training1 
# 初始化机器人，扫码登录
bot = Bot()

#搜索名称含有 "王小小" 的男性苏州好友
my_friend = bot.friends().search('王小小') [0]

print(my_friend)
my_friend.send('请给我分享一篇文章')
@bot.register(my_friend,'Sharing')
def auto_reply(msg):
        url = msg.url
        print (url)
        stats_msg = d12_training1.stats(url)
        msg.reply(stats_msg)
    
embed()