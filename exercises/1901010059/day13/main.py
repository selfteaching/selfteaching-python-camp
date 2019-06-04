from wxpy import Bot,Message,embed

bot = Bot()
my_friend = bot.friends().search('武曲63')  #定位朋友
#预先注册，利用Bot.register()完成
#Bot.register(chats=None,msg_types=None,except_self=True,run_async=True,enable=True)
@bot.register(chats = my_friend,msg_types = 'Sharing',except_self = True)
def auto_reply(msg):
    import requests
    from pyquery import PyQuery
#r = requests.get('https://api.github.com/user', auth=('user', 'pass')) 官方事例
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    from mymodule.stats_word import stats_text as a
    msg1 = dict(a(content,20))
    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    import pandas as pd
    from pandas import DataFrame,Series
    plt.rcParams['font.sans-serif']=['SimHei']
    group_x = list(msg1.keys())
    group_y = list(msg1.values())
    df = pd.DataFrame(group_y,index = group_x)
    df.plot(kind = 'barh')
    
    plt.savefig('day13.png')
    
    msg.reply_image('day13.png')
embed()