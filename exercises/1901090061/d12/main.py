import logging
import requests
import pyquery 
from wxpy import *
from mymodule import stats_word
logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|%(message)s',level=logging.DEBUG)
def get_artical(url):
    r = requests.get(url)
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()    
def main():
    bot = Bot()
    my_friend = bot.friends()
    @bot.register(my_friend,SHARING)
    def handler(msg):
        artical = get_artical(msg.url)
        result = stats_word.stats_text_cn(artical,100)
        print(result)
        return result
        
    embed()
if __name__ =='__main__':
    main()