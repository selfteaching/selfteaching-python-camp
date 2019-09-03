from pyquery import PyQuery
from wxpy import *
import yagmail
import requests
import getpass
import mymodule.stats_word

bot = Bot()
myself = bot.self
bot.file_helper.send('Hello from wxpy!')

@bot.register()
def print_messages(msg):
        
        if msg.type == SHARING:
                r=requests.get(msg.url,auth=('user','pass')) 
                document=PyQuery(r.text)
                content=document('#js_content').text()
                counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 100)
                counter_cn_string = str(counter_cn_dict)
                msg.reply(counter_cn_string)
        
embed()

