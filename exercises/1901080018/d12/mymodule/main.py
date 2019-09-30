from wxpy import *
bot = Bot()
my_friend = bot.friends().search("波罗",sex=MALE,city='广州')[0]
my_friend.send('我找到你了')
@bot.register(chats =None,msg_types = 'Sharing',except_self = True)
def auto_reply(msg):
    import requests
    from pyquery import PyQuery
    import stats_word
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(response.text)
    content = document('#js_content').text()
    list1 = stats_word.stats_text(content,100)
    str1 = "".join([str(i) for i in list1])
    return str1
embed()