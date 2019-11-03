from wxpy import *
bot = Bot(cache_path=True,console_qr=2)
friend = bot.friends()
@bot.register(friend,SHARING)
def counter(msg):
    import requests
    response = requests.get(msg.url,auth = ('user','path'))
    from pyquery import PyQuery
    document = PyQuery(response.text)
    content = document('#js_content').text()
    from mymodule.stats_word import stats_text_3 as f
    result =f(content)
    import matplotlib.pyplot as plt
    import numpy as np
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()
    word = []
    frequency = []
    for i in result:
        word.append(i[0])
        frequency.append(i[1])
    y_pos = np.arange(len(word))
    error = np.random.rand(len(word))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax.barh(y_pos, frequency, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(word)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('词语出现次数')
    ax.set_title('词频统计结果')
    plt.savefig('q.png')
    msg.reply_image('q.png')    
embed()