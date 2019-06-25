from wxpy import *
import d11_training1

bot = Bot()

my_friend = bot.friends().search('西门阿')[0]
my_friend.send('做测试啊')


@bot.register(msg_types=SHARING)#监听好友分享的消息
def auto_reply(msg):
    print(msg)
    if msg.type == "Sharing":
        str_word=[]
        str_num=[]
 
        url = msg.url
        str1 = d11_training1.get_url_message(url)
        print(str1)
        for i in str1:
            str_word.append(i[0])
            str_num.append(i[1])
        print(str_word)
        print(str_num)

        my_friend.send(msg)
        my_friend.send(str1)
       
        my_friend.send_image('chart.jpg')

embed()