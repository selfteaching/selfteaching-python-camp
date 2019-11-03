from wxpy import *
bot = Bot()
friend = bot.friends()
@bot.register(friend,SHARING)
def counter(msg):
    import requests
    response = requests.get(msg.url,auth = ('user','path'))
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text()
    from mymodule.stats_word import stats_text_3 as f
    print(f(content))
    msg.reply(f(content))
embed()