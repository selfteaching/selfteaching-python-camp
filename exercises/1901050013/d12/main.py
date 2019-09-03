import requests
from pyquery import PyQuery
from mymodule.stats_word import stats_text_cn
from wxpy import *

bot = Bot() # log in the wechat.
my_friend = bot.friends() #choose all the friends.
@bot.register(my_friend,SHARING) # collecting the sharing from friends.
def auto_reply(msg): # define how to reply to the friends.
    response = requests.get(msg.url) # acquire the article link.
    document = PyQuery(response.text)
    content = document('#js_content').text() #acquire the article content.
    result = str(stats_text_cn(content)) #convert the list type into string type.
    print(result)
    return result #return the result to the friends.


embed() #keep collecting the sharing from friends.


