import sys
sys.path.append('/anaconda3/lib/python3.7/site-packages')
from mymodule import stats_word
import requests
import pyquery
import yagmail
import getpass
from pyquery import PyQuery
from wxpy import*

bot=Bot()
my_friend=bot.friends().search('没没')
my_friend.send('hello you!')

@bot.register(my_friends,SHARING)

def friend_sharing(msg):
    address=msg.url
    reponse=requests.get(address)
    document=PyQuery(reponse.text)
    content=document('#js_content').text()
    text=stats_word.stats_text_cn(content,100)
    text1=str(text)
    my_friend.send(text1)
    
embed()
