from wxpy import *
bot =Bot(cache_path=True)

#机器人账号自身
myself= bot.self

#向文件传数助手发送消息

bot.file_helper.send('hello from wxpy!')
my_friend = bot.friends().search('yan',sex =FEMALE,city ="上海")[0]

my_friend.send('hello')




