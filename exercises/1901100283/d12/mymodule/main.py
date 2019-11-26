#将实战项⽬目1的功能包装集成到个⼈人微信
from wxpy import *
bot = Bot()
my_friend=bot.friends()
@bot.register(my_friend,SHARING)
def get_friend_url(msg):
    if isinstance(msg.type,SHARING):
        import requests
        response=requests.get(msg.url)
        from pyquery import PyQuery
        document=PyQuery(response.text)
        content=document('#js_content').text()
        from stats_word import stats_text_cn
        body=str(stats_text_cn(content))
        msg.reply(body)
embed()