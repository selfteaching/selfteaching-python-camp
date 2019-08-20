from wxpy import *

bot = Bot()
my_friend = bot.friends().search('月生')[0]
@bot.register(my_friend, SHARING)
def get_url(mgs):
    n = mgs.url 
    import requests
    from pyquery import PyQuery
    r = requests.get(n)
    document = PyQuery(r.text)
    content = document('#js_content').text()
    from mymodule import stats_word
    li1 = stats_word.stats_text_cn(content, 100)
    s = ''
    li2 = []
    for i in li1:
        li2.append('\'{}\':{}；'.format(i[0],i[1]))
    li2.insert(0, '前{}个单词及其出现次数：'.format(len(li2)))
    s1 = s.join(li2)
    my_friend.send(s1)

embed()









