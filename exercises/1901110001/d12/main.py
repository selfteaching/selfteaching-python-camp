import mymodule.stats_word
import requests
from pyquery import PyQuery
from wxpy import * 

def main():
    bot=Bot() 
    my_friend=bot.friends()
    @bot.register(my_friend,SHARING)
    def auto_reply(msg):
        response=requests.get(msg.url)
        document=PyQuery(response.text)
        content=document('#js_content').text()
        result=mymodule.stats_word.stats_text_cn(content,count=100)
        return result 

if __name__=='__main__':
     main()