# Using wxpy to do the automatic reaply for sharing type
from wxpy import *
bot = Bot()
Chats=bot.friends()
# Doing the statistic for SHARING type
@bot.register(Chats,SHARING)
def print_statis(msg):
    # Import the 微信文章 from the chat
    import requests
    response=requests.get(msg.url)
    # Transer the 微信文章 to string type
    from pyquery import PyQuery
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    # Make the satistic of the frequency of the word and output as a string
    import stats_word
    stats = stats_word.stats_text_cn(content,10)
    # Value is used to store frequency, index is used to store words
    value = []
    index = []
    for unit in stats:
        # Control the spacing by adding two more space it the word is less than two
        value.append(unit[1])
        index.append(unit[0])
    # Create the plot
    import matplotlib.pyplot as plt
    scale = range(10)
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("微信公众号文章词频统计")
    plt.xlabel("词汇")
    plt.ylabel("词频")
    plt.bar(scale,value)
    plt.xticks(scale,index)
    msg.reply(plt.show())
embed()