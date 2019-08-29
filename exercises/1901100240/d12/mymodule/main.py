# Using wxpy to do the automatic reaply for sharing type
from wxpy import *
bot = Bot()

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
    stats = stats_word.stats_text_cn(content,100)
    string=str('')      # Create a string to store the result
    for unit in stats:
    # Control the spacing by adding two more space it the word is less than two
        if len(unit[0]) <= 2:
            string += "'" + unit[0] + "'的频率是:    " + str(unit[1]) + "\n"
        elif len(unit[0]) == 3:
            string += "'" + unit[0] + "'的频率是:  " + str(unit[1]) + "\n"
    msg.reply(string)
embed()