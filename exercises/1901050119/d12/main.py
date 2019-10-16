import requests
from pyquery import PyQuery
from wxpy import *
from mymodule import stats_word

def get_text(url):   
    response = requests.get(url)
    document = PyQuery(response.text)
    return document('#js_content').text()

def main():
    bot = Bot()
    friends = bot.friends().search('Galaxy', sex = FEMALE, city = "西安")
    
    @bot.register(friends, SHARING)
    def handler(msg):
        content = get_text(msg.url)
        result = stats_word.stats_text_cn(content, 100)
        msg.reply(str(result))
        
    embed()


if __name__ == "__main__":
    main()
