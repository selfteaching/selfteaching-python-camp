from wxpy import *

bot = Bot()

bot.file_helper.send('hello world!')

my_friend = bot.friends().search('以武入道')[0]
my_friend.send('Hello WeChat!')

#def reply_my_friend(msg):
  #  return 'received: {} ({})'.format(msg.text, msg.type)
@bot.register(chats='以武入道',msg_types='sharing')
def replytext(msg):
    print(msg)
 

bot.join()
print("ending")