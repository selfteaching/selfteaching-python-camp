from wxpy import *
import  requests
from pyquery import PyQuery
import re
import jieba
from collections import Counter
import getpass

bot = Bot(cache_path= True)

@bot.register(Friend)
def print_others(msg):
    print(msg)
    if msg.type == 'sharing':
        response = requests.get(msg.url)
        document = PyQuery(response.text)
        content = document('p').text
        content = re.sub('[a-zA-Z0-9’!"%&\'^\s+|\s+$()*+,-./:;，。?、…？“”‘’！]+',"",content)
        seg_list = jieba.cut(content, cut_all=True)
        result = Counter()
        for seg in seg_list:
            if len(seg) > 1:
                result [seg] = result [seg] + 1

        mydic = result.most_common(100)
        mustr = str(mydic)
        msg.sender.send(mystr)

embed()