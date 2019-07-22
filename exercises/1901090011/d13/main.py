from wxpy import *

bot = Bot()
my_friend = bot.friends()  #定位朋友
#預先註冊，利用Bot.register()完成
#Bot.register(chats=None,msg_types=None,except_self=True,run_async=True,enable=True)
@bot.register(my_friend,SHARING) #接受分享類消息
def auto_reply(msg):
    import requests
    from pyquery import PyQuery
#r = requests.get('https://api.github.com/user', auth=('user', 'pass')) 官方示例
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    content = document('#js_content').text()
    from mymodule.stats_word import stats_text as a
    msg1 = dict(a(content,20))
    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm #為了顯示中文替換字體
    import pandas as pd #Pandas 提供兩種主要的資料結構，Series 與 DataFrame。Series 顧名思義就是用來處理時間序列相關的資料(如感測器資料等)，主要為建立索引的一維陣列。DataFrame 則是用來處理結構化(Table like)的資料，有列索引與欄標籤的二維資料集，例如關聯式資料庫、CSV 等等。 
    from pandas import DataFrame,Series
    plt.rcParams['font.sans-serif']=['SimHei']
    group_x = list(msg1.keys())
    group_y = list(msg1.values())
    df = pd.DataFrame(group_y,index = group_x)
    df.plot(kind = 'barh')
    
    plt.savefig('day13.png')
    
    msg.reply_image('day13.png') #將結果返回給發送消息的好友
embed() #賭塞線程保持監聽