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
    li1 = stats_word.stats_text_cn(content, 10)
    li2 = []
    li3 = []
    for i in li1:
        li2.append(i[0])
        li3.append(i[1])
    import matplotlib
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.barh(range(len(li2)), li3, tick_label=li2)
    plt.savefig('day13.png')
    mgs.reply_image('day13.png')

embed()









